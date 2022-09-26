new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        the_anonymus_list: [],

    },
    methods: {
        get_user_anonymus: function () {
            var self = this;
            axios.get('/api/list/capture/data/').then(function name(response) {
                self.the_anonymus_list = response.data
            })
        },        
    },
    beforeMount(){
        this.get_user_anonymus()
    },
});