new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        product_list: [],

    },
    methods: {
        get_product_list: function () {
            var self = this;
            axios.get('/api/list/producto/').then(function name(response) {
                self.product_list = response.data
            })
        },
        add_seguimiento: function (pk_id) {
            var self = this;
            var data = {
                'producto': pk_id,
            }
            
            axios.post('/api/capture/data/', data).then(function name(response) {
            })
        },
        
    },
    beforeMount(){
        this.get_product_list()
    },
});