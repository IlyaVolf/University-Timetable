<template>
  <div class="jumbotron horizontal-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
      <div class="row">
         <div class="col-sm-12">
          <p>Classrooms</p>
          <hr><br>

          <!-- Alert Msg-->
          <button type="button" class="btn btn-success btn-sm">Add Classroom</button>
          <br><br>
          <table class="table table-hover">
            <!-- Table Head-->
            <thead>
              <tr>
                <!-- Table header cells-->
                <th scope="col">id</th>
                <th scope="col">Number</th>
                <th scope="col">Type of class</th>
                <th scope="col">Class</th>
                <th scope="col">Year of study</th>
              </tr>
            </thead>
            <tbody>
              <tr> <!--v-for="faculty, index in faculties" :key="index">-->
                <td>DO</td>
                <td>DO</td>
                <td>DO</td>
                <td>DO</td>
                <td>DO</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
         </div> 
      </div>
     
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
      return {
        groups:[],
      };
    },

    methods:{
      getGroups() {
        const path = 'http://localhost:5000/groups';
        axios.get(path)
        .then((res) => {
          this.groups = res.data.groups;
        })
        .catch((err) => {
          console.error(err);
        });
      },
    },
    created() {
      this.getGroups();
    }
}
</script>
