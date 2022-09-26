new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        user_list: [],
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        first_name_edit: '',
        last_name_edit: '',
        email_edit: '',
        user_id: '',
        delete_user_id:'',
        x_error_update: false,
        x_error_save: false,
        error_update: [],
        error_save: [],
        form_delete: false,
    },
    methods:{   
        get_list_users: function (params) {
            var self = this;
            axios.get('/api/list/user/').then(function name(response) {
                self.user_list = response.data
            })
        },
        add_user:function (){
            var self = this;
            var data = {
                'username': self.username,
                'first_name': self.first_name,
                'last_name':self.last_name,
                'email': self.email,
                'password':self.password,
            }
            axios.post('/api/create/user/', data).then(function name(response) {
                self.username = ''
                self.first_name = ''
                self.last_name = ''
                self.email = ''
                self.password = ''
                self.get_list_users()
                self.form_user = true
            }).catch(function (error) {
                self.x_error_save = true
                self.error_save = error.response.data
            });
        },
        get_user:function (pk_id){
            var self = this;
            axios.get('/api/detail/user/'+pk_id+'/').then(function name(response) {
                self.username_edit = response.data[0].username
                self.first_name_edit = response.data[0].first_name
                self.last_name_edit = response.data[0].last_name
                self.email_edit = response.data[0].email
                self.password_edit = response.data[0].password
                self.user_id = response.data[0].id
            })
        },
        edit_user:function (){
            var self = this;
            var data = {
                'first_name': self.first_name_edit,
                'last_name':self.last_name_edit,
                'email': self.email_edit,
            }
            axios.put('/api/update/user/'+self.user_id+'/', data).then(function name(response) {
                self.get_list_users()
            }).catch(function (error) {
                self.x_error_update = true
                self.error_update = error.response.data
            });
        },
        get_delete_user:function (pk_id){
            var self = this;
            self.delete_user_id = pk_id
        },
        remove_user:function (){
            var self = this;
            axios.delete('/api/delete/user/' + self.delete_user_id).then(function name(response) {
                self.get_list_users()
            })
        },
    },
    beforeMount(){
        this.get_list_users()
    },
});
  