


const vm = new Vue({
    el: '#incidentContainer',
    delimiters: ["[[","]]"],
    data: {
     incident: []
    },

    mounted() {
            this.getIncident()
    },

    methods: {
        getIncident () {
            axios.get('api/v1/incident?format=json')
              .then(function (response) {
                vm.incident = response.data[0]

                console.log(response);
                console.log(incident)
              })
              .catch(function (error) {
                console.log(error);
              })
          }
    },
})