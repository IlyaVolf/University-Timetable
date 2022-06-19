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
        <button type="button" class="btn btn-success btn-sm" v-b-modal.generatedClass-modal>Add Incremental </button>
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
              <th scope="col">№</th>
              <!--<th scope="col">TeacherId</th> -->
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
              <td>{{generatedClass.groupsStr}}</td>
              <td>{{generatedClass.dayStr}}</td>
              <td>{{generatedClass.classNumber}}</td>
           <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteGeneratedClass(generatedClass)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        
        <!-- Footer -->
        <Footer class="bg-primary text-white text-center" style="border-radius:10px">Copyright &copy;. All Rights Reserved 2022.</Footer>

      </div>
    </div>

    <!-- Start of Modal 1 -->
    <b-modal ref="addGeneratedClassModal"
         id="generatedClass-modal"
         title="Add a new generated class" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-faculty-generatedClass"
                  label="faculty:"
                  label-for="form-faculty-input">
      <b-form-input id="form-faculty-input"
                    type="text"
                    v-model="addGeneratedClassForm.faculty"
                    required
                    placeholder="Enter faculty">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-educationalProgram-generatedClass"
                  label="educationalProgram:"
                  label-for="form-educationalProgram-input">
          <b-form-input id="form-educationalProgram-input"
                        type="text"
                        v-model="addGeneratedClassForm.educationalProgram"
                        required
                        placeholder="Enter educationalProgram">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-specialization-generatedClass"
                  label="specialization:"
                  label-for="form-specialization-input">
          <b-form-input id="form-specialization-input"
                        type="text"
                        v-model="addGeneratedClassForm.specialization"
                        required
                        placeholder="Enter specialization">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-subject-generatedClass"
                  label="subject:"
                  label-for="form-subject-input">
          <b-form-input id="form-subject-input"
                        type="text"
                        v-model="addGeneratedClassForm.subject"
                        required
                        placeholder="Enter subject">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-semester-generatedClass"
                  label="semester:"
                  label-for="form-semester-input">
          <b-form-input id="form-semester-input"
                        type="text"
                        v-model="addGeneratedClassForm.semester"
                        required
                        placeholder="Enter semester">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-teacher-generatedClass"
                  label="teacher:"
                  label-for="form-teacher-input">
          <b-form-input id="form-teacher-input"
                        type="text"
                        v-model="addGeneratedClassForm.teacher"
                        required
                        placeholder="Enter teacher">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-typeOfClass-generatedClass"
                  label="typeOfClass:"
                  label-for="form-typeOfClass-input">
          <b-form-input id="form-typeOfClass-input"
                        type="text"
                        v-model="addGeneratedClassForm.typeOfClass"
                        required
                        placeholder="Enter typeOfClass">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-auditory-generatedClass"
                  label="auditory:"
                  label-for="form-auditory-input">
          <b-form-input id="form-auditory-input"
                        type="text"
                        v-model="addGeneratedClassForm.auditory"
                        required
                        placeholder="Enter auditory">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-groups-generatedClass"
                  label="groups:"
                  label-for="form-groups-input">
          <b-form-input id="form-groups-input"
                        type="text"
                        v-model="addGeneratedClassForm.groups"
                        required
                        placeholder="Enter groups">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-day-generatedClass"
                  label="day:"
                  label-for="form-day-input">
          <b-form-input id="form-day-input"
                        type="text"
                        v-model="addGeneratedClassForm.day"
                        required
                        placeholder="Enter day">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classNumber-generatedClass"
                  label="classNumber:"
                  label-for="form-classNumber-input">
          <b-form-input id="form-classNumber-input"
                        type="text"
                        v-model="addGeneratedClassForm.classNumber"
                        required
                        placeholder="Enter classNumber">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-teacherId-generatedClass"
                  label="teacherId:"
                  label-for="form-teacherId-input">
          <b-form-input id="form-teacherId-input"
                        type="text"
                        v-model="addGeneratedClassForm.teacherId"
                        required
                        placeholder="Enter teacherId">
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->
  </div>
  </div>
</template>



<script>
import axios from 'axios';
export default {
  data() {
    return {
      generatedClasses: [],
      addGeneratedClassForm: {
        faculty: '',
        educationalProgram: '',
        specialization:'',
        subject:'',
        semester:'',
        teacher:'',
        typeOfClass: '',
        auditory: '',
        groups: '',
        day: '',
        classNumber: '',
        teacherId: '',
      },
    };
  },
  methods: {
    // 1 GET METHOD
    getGeneratedClasses() {
      const path = 'http://127.0.0.1:5000/generatedClasses';
      axios.get(path)
        .then((res) => {
          this.generatedClasses = res.data.generatedClasses;
        })
        .catch((error) => {
          if(error.response.data.error != null) {
            alert("Error: " + error.response.data.error)
            console.error(error);
            if(error.response.status == 401) {
              window.location = 'http://127.0.0.1:8080/login';
            }
          }
        });
    },


    addGeneratedClasses(payload) {
      const path = `http://127.0.0.1:5000/addman?faculty=${payload.faculty.replaceAll(' ','+')}&educationalProgram=${payload.educationalProgram.replaceAll(' ','+')}&specialization=${payload.specialization.replaceAll(' ','+')}&subject=${payload.subject.replaceAll(' ','+')}&semester=${payload.semester}&teacher=${payload.teacher.replaceAll(' ','+')}&typeOfClass=${payload.typeOfClass}&auditory=${payload.auditory}&groups=${payload.groups}&day=${payload.day}&classNumber=${payload.classNumber}&teacherId=${payload.teacherId}`;
      axios.get(path, payload)
        .then(() => {
          this.getSubjects();
          alert("Successfully added" )
          // for message alert
          this.message = 'Faculty added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          if(error.response.data.error != null) {
            alert("Error: " + error.response.data.error)
            console.error(error);
            if(error.response.status == 401) {
              window.location = 'http://127.0.0.1:8080/login';
            }
          }
          this.getSubjects();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addGeneratedClassForm.faculty = '';
        this.addGeneratedClassForm.educationalProgram = '';
        this.addGeneratedClassForm.specialization = '';
        this.addGeneratedClassForm.subject = '';
        this.addGeneratedClassForm.semester = '';
        this.addGeneratedClassForm.teacher = '';
        this.addGeneratedClassForm.typeOfClass = '';
        this.addGeneratedClassForm.auditory = '';
        this.addGeneratedClassForm.groups = '';
        this.addGeneratedClassForm.day = '';
        this.addGeneratedClassForm.classNumber = '';
        this.addGeneratedClassForm.teacherId = '';
        this.editForm.id = '';
        this.editForm.faculty = '';
        this.editForm.educationalProgram = '';
        this.editForm.specialization = '';
        this.editForm.subject = '';
        this.editForm.semester = '';
        this.editForm.teacher = '';
        this.editForm.typeOfClass = '';
        this.editForm.auditory = '';
        this.editForm.groups = '';
        this.editForm.day = '';
        this.editForm.classNumber = '';
        this.editForm.teacherId = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGeneratedClassModal.hide();
      const payload = {
        faculty: this.addGeneratedClassForm.faculty,
        educationalProgram: this.addGeneratedClassForm.educationalProgram,
        specialization: this.addGeneratedClassForm.specialization,
        subject: this.addGeneratedClassForm.subject,
        semester: this.addGeneratedClassForm.semester,
        teacher: this.addGeneratedClassForm.teacher,
        typeOfClass: this.addGeneratedClassForm.typeOfClass,
        auditory: this.addGeneratedClassForm.auditory,
        groups: this.addGeneratedClassForm.groups,
        day: this.addGeneratedClassForm.day,
        classNumber: this.addGeneratedClassForm.classNumber,
        teacherId: this.addGeneratedClassForm.teacherId,
      };
      this.addGeneratedClasses(payload);
      this.initForm();
    },

    onReset(e) {
      e.preventDefault();
      this.$refs.addGeneratedClassForm.hide();
      this.initForm();
    },
    generate(payload) {
      const path = 'http://127.0.0.1:5000/generate';
      axios.get(path, payload)
        .then(() => {
          this.getGeneratedClasses();
          
          // for message alert
          this.message = 'Generated added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          if(error.response.data.error != null) {
            alert("Error: " + error.response.data.error)
            console.error(error);
            if(error.response.status == 401) {
              window.location = 'http://127.0.0.1:8080/login';
            }
          }
          this.getGeneratedClasses();
        });
    },
    overgenerate(payload) {
      const path = 'http://127.0.0.1:5000/overgenerate';
      axios.get(path, payload)
        .then(() => {
          this.getGeneratedClasses();
          
          // for message alert
          this.message = 'Generated added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          if(error.response.data.error != null) {
            alert("Error: " + error.response.data.error)
            console.error(error);
            if(error.response.status == 401) {
              window.location = 'http://127.0.0.1:8080/login';
            }
          }
          this.getGeneratedClasses();
        });
    },

    removeGeneratedClass(id) {
    const path = `http://127.0.0.1:5000/removeman/${id}`;
    axios.get(path)
      .then(() => {
        this.getGeneratedClasses();
        this.message = 'Info Removed 🗑️!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        if(error.response.data.error != null) {
            alert("Error: " + error.response.data.error)
            console.error(error);
            if(error.response.status == 401) {
              window.location = 'http://127.0.0.1:8080/login';
            }
          }
        this.getSubjects();
      });
  },
  // Handle Delete Button
  deleteGeneratedClass(generatedClass) {
    this.removeGeneratedClass(generatedClass.id);
  },
   
  },
  created() {
    this.getGeneratedClasses();
  }
}
</script>
