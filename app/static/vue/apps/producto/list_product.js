new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        product_list: [],
        mark_list: [],
        type_product_list: [],
        x_error_update: false,
        x_error_save: false,
        error_update: [],
        error_save: [],
        sku: '',
        nombre: '',
        precio: '',
        stock: '',
        marca: '',
        tipo_producto: '',
        descripcion: '',
        delete_product_id: '',
        sku_edit: '',
        nombre_edit: '',
        precio_edit: '',
        stock_edit: '',
        marca_edit: '',
        tipo_producto_edit: '',
        descripcion_edit: '',
        product_id: '',
    },
    methods: {
        get_list_products: function () {
            var self = this;
            axios.get('/api/list/producto/').then(function name(response) {
                console.log(response.data)
                self.product_list = response.data
            })
        },
        add_product: function () {
            var self = this;
            var data = {
                'sku': self.sku,
                'nombre': self.nombre,
                'precio': self.precio,
                'stock': self.stock,
                'marca': self.marca,
                'tipo_producto': self.tipo_producto,
                'descripcion': self.descripcion,
            }

            axios.post('/api/create/producto/', data).then(function name(response) {
                self.sku = ''
                self.nombre = ''
                self.precio = ''
                self.stock = ''
                self.marca = ''
                self.descripcion = ''
                self.tipo_producto = ''
                self.get_list_products()
            }).catch(function (error) {
                self.x_error_save = true
                self.error_save = error.response.data
            });
        },
        get_product: function (pk_id) {
            var self = this;
            axios.get('/api/detail/producto/'+pk_id+'/').then(function name(response) {
                self.sku_edit = response.data[0].sku
                self.nombre_edit = response.data[0].nombre
                self.precio_edit = response.data[0].precio
                self.stock_edit = response.data[0].stock
                self.marca_edit = response.data[0].marca
                self.descripcion_edit = response.data[0].descripcion
                self.tipo_producto_edit = response.data[0].tipo_producto
                self.product_id = response.data[0].id
            })
        },
        edit_product: function () {
            var self = this;
            var data = {
                'nombre': self.nombre_edit,
                'precio': self.precio_edit,
                'stock': self.stock_edit,
                'descripcion': self.descripcion_edit,
            }
            axios.put('/api/update/producto/'+self.product_id+'/', data).then(function name(response) {
                self.get_list_products()
            }).catch(function (error) {
                self.x_error_update = true
                self.error_update = error.response.data
            });
        },
        get_delete_product: function (pk_id) {
            var self = this;
            self.delete_product_id = pk_id
        },
        remove_product: function () {
            var self = this;
            axios.delete('/api/delete/producto/' + self.delete_product_id).then(function name(response) {
                self.get_list_products()
            })
        },
        get_marca: function () {
            var self = this;
            axios.get('/api/list/marca/').then(function name(response) {
                console.log(response.data)
                self.mark_list = response.data
            })
        },
        get_type_producto: function () {
            var self = this;
            axios.get('/api/list/tipo_producto/').then(function name(response) {
                console.log(response.data)
                self.type_product_list = response.data
            })
        },
    },
    beforeMount(){
        this.get_list_products()
        this.get_marca()
        this.get_type_producto()
    },
});