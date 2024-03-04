{
    'name': 'Transport Management System',
    'depends': [
        'stock_picking_batch',
        'fleet',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
    ],
    'installable': True,
    'application': True,
}
