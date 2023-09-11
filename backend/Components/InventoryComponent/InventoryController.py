from flask import Blueprint, request, jsonify, session
from functools import wraps
from Components.InventoryComponent.InventoryService import InventoryService

inventory_blueprint = Blueprint('inventory', __name__)

@inventory_blueprint.route('/inventory/add', methods=["POST"])
def addProduct():
    try:
        data = request.get_json()
        part_number = data.get('part_number')
        quantity = data.get('quantity')
        nomenclature = data.get('nomenclature')
        haz_item = data.get('haz_item')
        remarks = data.get('remarks')
        unit_price = data.get('unit_price')
        location = data.get('location')
        project_tag = data.get('project_tag')
        jcn = data.get('jcn')

        if not all([part_number, quantity, nomenclature, haz_item, remarks, unit_price, location, project_tag, jcn]):
            return jsonify({"error": "All fields are required!"}), 400

        return InventoryService.addProduct(part_number, quantity, nomenclature, haz_item, remarks, unit_price, location, project_tag, jcn), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@inventory_blueprint.route('/inventory')
def displayProducts():
    return InventoryService.displayProducts()
@inventory_blueprint.route('/inventory/<int:id>')
def returnProductById():
        pass

@inventory_blueprint.route('/inventory/update')
def updateProduct():
        pass


@inventory_blueprint.route('/inventory/delete/<int:id>')
def deleteProduct():
        pass
