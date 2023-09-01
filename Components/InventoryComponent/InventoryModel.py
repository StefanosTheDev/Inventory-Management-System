# InventoryModel.py
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from ..UserComponent.UserModel import Base  # Importing the Base from UserModel

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, Sequence('inventory_id_seq'), primary_key=True)
    product_name = Column(String(100), nullable=False)
    product_type = Column(String(50), nullable=False)
    product_price = Column(Integer, nullable=False)  # You might want to use Float or Decimal for real-world currency values
    product_quantity = Column(Integer, nullable=False)
    associated_project = Column(String(100))
    
    # Linking each inventory item to a role
    role = Column(String(50), ForeignKey('users.role'), nullable=False)
