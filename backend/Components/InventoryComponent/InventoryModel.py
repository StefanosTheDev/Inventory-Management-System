
from extension import db

class InventoryModel(db.Model):
    __tablename__ = 'inventory'
    
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(20))
    quantity= db.Column(db.Integer)
    nomenclature = db.Column(db.String(100))
    haz_item = db.Column(db.String(50))
    remarks = db.Column(db.String(100))
    unit_price = db.Column(db.Integer)
    location = db.Column(db.String(100))
    project_tag = db.Column(db.String(100))
    jcn = db.Column(db.Integer)

    def __str__(self):  
        return str(self.json())

    def __repr__(self): 
        return self.__str__()

    def json(self):
        return {
            'id': self.id,
            'part_number': self.part_number,
            'quantity': self.quantity,  # Ideally you'd never print or share this
            'nomenclature': self.nomenclature,
            'haz_item': self.haz_item,
            'remarks': self.remarks,
            'unit_price': self.unit_price,
            'location': self.location,
            'project_tag': self.project_tag,
            'jcn': self.jcn
        }