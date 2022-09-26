new Vue({
    el: 'app',
    delimiters: ['{$', '$}'],
    mounted() {
        var self = this;
        // cargamos lista de usuarios
        axios.get('/api/list-user/').then(function (response) {
            console.log(response.data);
            self.user_list = response.data;
        })
        .catch(function (error) {
            console.log(error);
        });
    },
    data: {
        user_list:[],
        kword:'',
    },
  })
  