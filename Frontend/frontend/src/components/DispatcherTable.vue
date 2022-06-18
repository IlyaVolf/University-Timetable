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
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" @click="generate()">Generate</button>
        <button type="button" class="btn btn-success btn-sm" @click="overgenerate()">Overgenerate</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Faculty</th>
              <th scope="col">Program</th>
              <th scope="col">Specialization</th>
              <th scope="col">Subject</th>
              <th scope="col">Semester</th>
              <th scope="col">Teacher</th>
              <th scope="col">Class</th>
              <th scope="col">Auditory</th>
              <th scope="col">Groups</th>
              <th scope="col">Day</th>
              <th scope="col">ClassNumber</th>
              <th scope="col">TeacherId</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(generatedClass, index) in generatedClasses" :key="index">
              <!-- td : table data -->
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
      generatedClasses: [],
    };
  },
  methods: {
    // 1 GET METHOD
    getGeneratedClasses() {
      const path = 'http://localhost:5000/generatedClasses';
      axios.get(path)
        .then((res) => {
          this.generatedClasses = res.data.generatedClasses;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    generate(payload) {
      const path = 'http://localhost:5000/generate';
      axios.get(path, payload)
        .then(() => {
          this.getGeneratedClasses();
          
          // for message alert
          this.message = 'Generated added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getGeneratedClasses();
        });
    },
    overgenerate(payload) {
      const path = 'http://localhost:5000/overgenerate';
      axios.get(path, payload)
        .then(() => {
          this.getGeneratedClasses();
          
          // for message alert
          this.message = 'Generated added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getGeneratedClasses();
        });
    },
   
  },
  created() {
    this.getGeneratedClasses();
  }
}
</script>
