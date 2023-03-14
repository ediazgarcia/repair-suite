from utils.db import db


class Company(db.Model):
    __tablename__ = 'empresas'
    id_empresa = db.Column(db.Integer, primary_key=True)
    razon_social = db.Column(db.String(50), nullable=False)
    rnc_cedula = db.Column(db.String(20), unique=True, nullable=False)
    nombre_comercial = db.Column(db.String(100), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(30), unique=True, nullable=False)
    telefono = db.Column(db.String(12), nullable=False)
    logo_corp = db.Column(db.LargeBinary)
    direccion = db.Column(db.Text, nullable=False)
    provincia = db.Column(db.String(50), nullable=False)
    municipio = db.Column(db.String(50), nullable=False)
    creado = db.Column(db.TIMESTAMP(), default=db.func.current_timestamp())
    actualizado = db.Column(
        db.TIMESTAMP(),
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def __init__(self, razon_social, rnc_cedula, nombre_comercial, correo_electronico, telefono, logo_corp, direccion, provincia, municipio):
        self.razon_social = razon_social
        self.rnc_cedula = rnc_cedula
        self.nombre_comercial = nombre_comercial
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.logo_corp = logo_corp
        self.direccion = direccion
        self.provincia = provincia
        self.municipio = municipio
