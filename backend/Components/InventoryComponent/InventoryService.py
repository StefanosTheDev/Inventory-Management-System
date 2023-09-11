## Okay for the service. 
## We need to Create Read Update Delete JCNS. We also need an ADD TO Cart Feature
from Components.InventoryComponent.InventoryModel import InventoryModel
from flask import jsonify, session
from extension import db
class InventoryService:
    def addProduct(part_number, quantity, nomenclature, haz_item, remarks, unit_price, location, project_tag, jcn):
        try:
            # WHy did i ned to have an = to a part_number
            new_entry = InventoryModel(part_number=part_number, quantity=quantity, nomenclature=nomenclature, haz_item=haz_item, remarks=remarks, unit_price=unit_price, location=location, project_tag=project_tag, jcn=jcn)
            db.session.add(new_entry)
            db.session.commit()
            return jsonify({"Entry Added": new_entry.json()})
        except Exception as e:
            db.session.rollback()
            return jsonify({"Error": e})
        
            
    def displayProducts():
        try: 
            all_products = InventoryModel.query.all()
            if not all_products:
                raise Exception("No users were found in the database")
            products_json = [product.json() for product in all_products]
            return jsonify({'message': products_json})
        except Exception as error:
            print(error)
            return jsonify({'error': str(error)}), 400
    def returnProductById():
        pass
    def updateProduct():
        pass
    def deleteProduct():
        pass
    def addToCart():
        pass
