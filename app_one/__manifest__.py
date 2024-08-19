{
    'name' : "app one" ,
    'author': "omar abdelsamee",
    'category': '',
    'version': '17.0.0.1.0',
    'depends': [ 'base' , 'sale_management' , 'mail' , 'contacts',
                 ] ,
    'data' : [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_inheritance_view.xml',
        'views/res_partner_inheritance_view.xml',
        'views/building_view.xml',

    ],
    'application': True,

}