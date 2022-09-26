new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        mark_list: [],
        marca: '',
        marca_edit: '',
        x_error_save: '',
        x_error_update: '',
        delete_mark_id: '',
        marca_id: '',
        error_update: '',
    },
    methods: {
        get_list_mark: function () {
            var self = this;
            axios.get('/api/list/marca/').then(function name(response) {
                console.log(response.data)
                self.mark_list = response.data
            })
        },
        add_mark: function () {
            var self = this;
            var data = {
                'marca': self.marca,
            }
            axios.post('/api/create/marca/', data).then(function name(response) {
                self.marca = ''
                self.get_list_mark()
            }).catch(function (error) {
                self.x_error_save = true
                self.error_save = error.response.data
            });
        },
        get_mark: function (pk_id) {
            var self = this;
            axios.get('/api/detail/marca/'+pk_id+'/').then(function name(response) {
                self.marca_edit = response.data[0].marca
                self.marca_id = response.data[0].id
            })
        },
        edit_mark: function () {
            var self = this;
            var data = {
                'marca': self.marca_edit,
            }
            axios.put('/api/update/marca/'+self.marca_id+'/', data).then(function name(response) {
                self.get_list_mark()
            }).catch(function (error) {
                self.x_error_update = true
                self.error_update = error.response.data
            });
        },
        get_remove_mark: function (pk_id) {
            var self = this;
            self.delete_mark_id = pk_id
        },
        remove_mark: function () {
            var self = this;
            var data = {
                'activa': 0,
            }
            axios.put('/api/remove/marca/'+self.delete_mark_id+'/', data).then(function name(response) {
                self.get_list_mark()
            }).catch(function (error) {
                self.x_error_update = true
                self.error_update = error.response.data
            });
        },
    },
    beforeMount(){
        this.get_list_mark()
    },
});