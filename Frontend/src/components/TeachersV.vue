<template>
  <div class="jumbotron horizontal-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
      <div class="row">
         <div class="col-sm-12">
          <p>Teachers</p>
          <hr><br>

          <!-- Alert Msg-->
          <button type="button" class="btn btn-success btn-sm">Add Teacher</button>
          <br><br>
          <table class="table table-hover">
            <!-- Table Head-->
            <thead>
              <tr>
                <!-- Table header cells-->
                <th scope="col">id</th>
                <th scope="col">Name</th>
                <th scope="col">Can Work</th>
                <th scope="col">Can't Work</th>
                <th scope="col">Weight</th>
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
        teachers:[],
      };
    },

    methods:{
      getTeachers() {
        const path = 'http://localhost:5000/teachers';
        axios.get(path)
        .then((res) => {
          this.teachers = res.data.teachers;
        })
        .catch((err) => {
          console.error(err);
        });
      },
    },
    created() {
      this.getTeachers();
    }
}
</script>
