<template>
  <div class="jumbotron horizontal-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
      <div class="row">
         <div class="col-sm-12">
          <p>Games library</p>
          <hr><br>

          <!-- Alert Msg-->
          <button type="button" class="btn btn-success btn-sm">Add Game</button>
          <br><br>
          <table class="table table-hover">
            <!-- Table Head-->
            <thead>
              <tr>
                <!-- Table header cells-->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="game, index in gamestest" :key="index">
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

import axios from 'axios';
export default {
    data() {
      return {
        gamestest:[],
      };
    },

    methods:{
      getGames() {
        const path = 'http://localhost:5000/gamestest';
        axios.get(path)
        .then((res) => {
          this.gamestest = res.data.gamestest;
        })
        .catch((err) => {
          console.error(err);
        });
      },
    },
    created() {
      this.getGames();
    }
}
</script>
