new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        type_list: [],
        nombre_tipo: '',
        delete_type_id: '',
        nombre_tipo_edit: '',
        tipo_id: '',
    },
    methods: {
        get_list_type: function () {
            var self = this;
            axios.get('/api/list/tipo_producto/').then(function name(response) {
                console.log(response.data)
                self.type_list = response.data
            })
        },
        add_type: function () {
            var self = this;
            var data = {
                'nombre_tipo': self.nombre_tipo,
            }
            axios.post('/api/create/tipo_producto/', data).then(function name(response) {
                self.nombre_tipo = ''
                self.get_list_type()
            }).catch(function (error) {
                self.x_error_save = true
                self.error_save = error.response.data
            });
        },
        get_type: function (pk_id) {
            var self = this;
            axios.get('/api/detail/tipo_producto/'+pk_id+'/').then(function name(response) {
                self.nombre_tipo_edit = response.data[0].nombre_tipo
                self.tipo_id = response.data[0].id
            })
        },
        edit_type: function () {
            var self = this;
            var data = {
                'nombre_tipo': self.nombre_tipo_edit,
            }
            axios.put('/api/update/tipo_producto/'+self.tipo_id+'/', data).then(function name(response) {
                self.get_list_type()
            })
        },
        get_remove_type: function (pk_id) {
            var self = this;
            self.delete_type_id = pk_id
        },
        remove_type: function () {
            var self = this;
            var data = {
                'activa': 0,
            }
            axios.put('/api/remove/tipo_producto/'+self.delete_type_id+'/', data).then(function name(response) {
                self.get_list_type()
            })
        },
    },
    beforeMount(){
        this.get_list_type()
    },
});