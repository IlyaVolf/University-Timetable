<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Groups </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Group</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(group, index) in groupsForSchedule" :key="index">
                <td>
                    <a :href="'groups/' + group.name" >{{group.name}}</a> 
                </td>
                      
            </tr>
          </tbody>
        </table>
        
        <!-- Footer -->
        <Footer class="bg-primary text-white text-center" style="border-radius:10px">Copyright &copy;. All Rights Reserved 2022.</Footer>

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
      groupsForSchedule: [],
    };
  },
  message:'',
    methods: {
        // 1 GET METHOD
        getFaculties() {
        const path = 'http://127.0.0.1:5000/schedule/faculties/1';
        axios.get(path)
            .then((res) => {
            this.groupsForSchedule = res.data.groupsForSchedule;
            })
            .catch((error) => {
            console.error(error);
            });
        },
    },
    created() {
        this.getFaculties(); 
    },
}
</script>