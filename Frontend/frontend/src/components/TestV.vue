<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Generated Classes </h1>
        <hr><br>
        
         <!-- Alert -->
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">scheduleTeacher</th>
              <th scope="col">scheduleEntities[1][2]</th>
              <th scope="col">scheduleEntities[1]</th>
              
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <!--<tr v-for="(scheduleEntity, index) in scheduleTeachers" :key="index">-->
            <td>{{scheduleTeachers}}</td>
            <td>{{scheduleEntities[1][2][0].auditory}}</td>
            <td>{{scheduleEntities[[1]]}}</td>
            
            
              <!-- td : table data 
              <td>{{generatedClass.faculty}}</td>
              <td>{{generatedClass.educationalProgram}}</td>
              <td>{{generatedClass.specialization}}</td>
              <td>{{generatedClass.subject}}</td>
              <td>{{generatedClass.semester}}</td>
              <td>{{generatedClass.teacher}}</td>
              <td>{{generatedClass.typeOfClass}}</td>
              <td>{{generatedClass.auditory}}</td>
              <td>{{generatedClass.groups}}</td>
              <td>{{generatedClass.day}}</td>
              <td>{{generatedClass.classNumber}}</td>
              <td>{{generatedClass.teacherId}}</td>
            </tr>-->
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
      scheduleTeachers: [],
      scheduleEntities: [],
    };
  },
  methods: {
    // 1 GET METHOD
    getGeneratedClasses() {
      const path = `http://localhost:5000/schedule/teachers/4`;
      axios.get(path)
        .then((res) => {
          this.scheduleTeachers = res.data.scheduleTeachers
          this.scheduleEntities = this.scheduleTeachers.scheduleEntities
        })
        .catch((error) => {
          console.error(error);
        });
    },
   
  },
  created() {
    this.getGeneratedClasses();
  }
}
</script>
