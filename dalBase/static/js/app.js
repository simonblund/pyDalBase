
Vue.use(require('vue-moment'));
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
            axios.get('http://localhost:8000/dalBase/api/v1/incident?format=json')
              .then(function (response) {
                vm.incident = response.data[0]
              })
              .catch(function (error) {
                console.log(error);
              })
          },
          getUnderway () {
            axios.get('http://localhost:8000/dalBase/api/v1/underway?format=json')
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

const vm1 = new Vue({
    el: '#incidentReportsContainer',
    delimiters: ["[[","]]"],
    data: {
     incidentreports: [],
    },

    mounted() {
            this.getIncidentReports(),
    },

    methods: {
        getIncidentReports () {
            axios.get('/api/v1/incidentreport?format=json')
              .then(function (response) {
                vm1.incidentreports = response.data[0]
              })
              .catch(function (error) {
                console.log(error);
              })
          },

    },
})