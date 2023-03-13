from utils.db import db


class Client(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    tipo_doc = db.Column(db.String(20), nullable=False)
    num_doc = db.Column(db.String(20), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(50), unique=True, nullable=False)
    telefono = db.Column(db.String(12), nullable=False)
    ciudad = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.Text)
    creado = db.Column(db.TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    actualizado = db.Column(
        db.TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    empresa_id = db.Column(db.Integer, db.ForeignKey(
        'empresas.id_empresa', onupdate='RESTRICT', ondelete='CASCADE'))
    empresa = db.relationship("Empresa", back_populates="clientes")

    def __init__(self, nombre, apellido, tipo_doc, num_doc, correo_electronico, telefono, ciudad, direccion, empresa_id):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_doc = tipo_doc
        self.num_doc = num_doc
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.ciudad = ciudad
        self.direccion = direccion
        self.empresa_id = empresa_id
