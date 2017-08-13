
const vm = new Vue({
    el: '#incidentContainer',
    delimiters: ["[[","]]"],
    data: {
     incident: [],
     underways: []
    },

    mounted() {
            this.getIncident(),
            this.getUnderway()
    },

    methods: {
        getIncident () {
            axios.get('api/v1/incident?format=json')
              .then(function (response) {
                vm.incident = response.data[0]
              })
              .catch(function (error) {
                console.log(error);
              })
          },
          getUnderway () {
            axios.get('api/v1/underway?format=json')
              .then(function (response) {
                vm.underways = response.data
                console.log(response.data)
              })
              .catch(function (error) {
                console.log(error);
              })
          }
    },
})