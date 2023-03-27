from app import db

class Category(db.Model):
    # si no le pongo __tablename__ la tabla se llamara ifual que la clase
    __tablename__ = 'categorias' #nombre de la tabla
    idCategorias = db.Column(db.Integer, primary_key=True , autoincrement=True)
    catNombre = db.Column(db.String(50) , unique=True, nullable=False)
    
    def __repr__(self):
        return f'{self.catNombre}'