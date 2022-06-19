<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Educational Programs </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.educationalProgram-modal>Add Program</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Faculty</th>
              <th scope="col">Name</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(educationalProgram, index) in educationalPrograms" :key="index">
              <!-- td : table data -->
              <td>{{educationalProgram.faculty}}</td>
              <td>{{educationalProgram.educationalProgram}}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.educationalProgram-update-modal
                  @click="editEducationalProgram(educationalProgram)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteEducationalProgram(educationalProgram)">Delete</button>
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
    <b-modal ref="addEducationalProgramModal"
         id="educationalProgram-modal"
         title="Add a new program" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-facultyId-educationalProgram"
                  label="FacultyId:"
                  label-for="form-facultyId-input">
                  
          <b-form-input
            id="form-facultyId-input"
            v-model="addEducationalProgramForm.facultyId"
            required>
          </b-form-input>
     <!---- <b-form-select id="form-facultyId-input"
                    type="text"
                    v-model="addEducationalProgramForm.facultyId"
                    required
                    placeholder="Enter facultyId">
                    <select class="form-select" v-model="Faculty">
                            <option v-for="(faculty, index) in faculties" :key="index">
                            {{faculty.faculty}}
                            </option>
                        </select>  
      </b-form-select>-->
    </b-form-group>

    <b-form-group id="form-educationalProgram-educationalProgram"
                  label="educationalProgram:"
                  label-for="form-educationalProgram-input">
                  
      <b-form-input id="form-educationalProgram-input"
                    type="text"
                    v-model="addEducationalProgramForm.name"
                    required
                    placeholder="Enter Name">
      </b-form-input>
    </b-form-group>


      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editEducationalProgramModal"
         id="educationalProgram-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-facultyId-edit-educationalProgram"
                label="facultyId:"
                label-for="form-facultyId-edit-input">
      <b-form-input id="form-facultyId-edit-input"
                    type="text"
                    v-model="editForm.facultyId"
                    required
                    placeholder="Enter facultyId">
      </b-form-input>
      <!--<b-form-select
            id="form-facultyId-input"
            v-model="editForm.facultyId"
            :options="faculties.id"
            required>
      </b-form-select>-->
  </b-form-group>

  <b-form-group id="form-name-edit-educationalProgram"
                label="Name:"
                label-for="form-name-edit-input">
      <b-form-input id="form-name-edit-input"
                    type="text"
                    v-model="editForm.name"
                    required
                    placeholder="Enter Name">
      </b-form-input>
    </b-form-group>

  <b-button-group>
    <b-button type="submit" variant="outline-info">Update</b-button>
    <b-button type="reset" variant="outline-danger">Cancel</b-button>
  </b-button-group>
  </b-form>
</b-modal>
<!-- end of modal 2 -->
  </div>
  </div>
</template>



<script>
import axios from 'axios';
export default {
  data() {
    return {
      faculties:[],
      educationalPrograms: [],
      addEducationalProgramForm: {
        facultyId: '',
        name: '',
      },
      editForm: {
        id: '',
        facultyId: '',
        name: '',
      },
      form: {
          email: '',
          name: '',
          food: null,
          checked: []
        },
        foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        show: true
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getEducationalPrograms() {
      const path = 'http://127.0.0.1:5000/educationalPrograms';
      axios.get(path)
        .then((res) => {
          this.educationalPrograms = res.data.educationalPrograms;
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
    getFaculties() {
      const path = 'http://127.0.0.1:5000/faculties';
      axios.get(path)
        .then((res) => {
          this.faculties = res.data.faculties;
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
    // 2 Add Teacher Button
    addEducationalProgram(payload) {
      const path = `http://127.0.0.1:5000/educationalPrograms?facultyId=${payload.facultyId}&name=${payload.name}`;
      axios.post(path, payload)
        .then(() => {
          this.getEducationalPrograms();
          this.getFaculties();
          
          // for message alert
          this.message = 'Educational Program added !';
          
          // to show message when teacher is added
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
          this.getEducationalPrograms();
          this.getFaculties();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addEducationalProgram.facultyId = '';
        this.addEducationalProgram.name = '';
        this.editForm.id = '';
        this.editForm.facultyId = '';
        this.editForm.name = '';
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.form.email = ''
        this.form.name = ''
        this.form.food = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      this.$refs.addEducationalProgramModal.hide();
      const payload = {
        facultyId: this.addEducationalProgramForm.facultyId,
        name: this.addEducationalProgramForm.name,
      };
      this.addEducationalProgram(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editEducationalProgramModal.hide();
    const payload = {
      facultyId: this.editForm.facultyId,
      name: this.editForm.name,
    };
    this.updateEducationalProgram(payload, this.editForm.id);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addEducationalProgramModal.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
updateEducationalProgram(payload, id) {
  const path = `http://127.0.0.1:5000/educationalPrograms/${id}?facultyId=${payload.facultyId}&name=${payload.name}`;
  axios.put(path, payload)    
    .then(() => {
      this.getEducationalPrograms();
      this.message = 'Information updated ⚙️!';
      this.showMessage =  true;
    })
    .catch((error) => {
      if(error.response.data.error != null) {
            alert("Error: " + error.response.data.error)
            console.error(error);
            if(error.response.status == 401) {
              window.location = 'http://127.0.0.1:8080/login';
            }
          }
      this.getEducationalPrograms();
    });
},
 // Handle Update Button 
editEducationalProgram(educationalProgram) {
  this.editForm = educationalProgram;
},
// 5 Handle reset / cancel button click
onResetUpdate(e) {
  e.preventDefault();
  this.$refs.editEducationalProgramModal.hide();
  this.initForm();
  this.getEducationalPrograms(); 
},
// Remove teacher [ Delete Button ]
removeEducationalProgram(id) {
  const path = `http://127.0.0.1:5000/educationalPrograms/${id}`;
  axios.delete(path)
    .then(() => {
      this.getEducationalPrograms();
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
      this.getEducationalPrograms();
    });
},
// Handle Delete Button
deleteEducationalProgram(educationalProgram) {
  this.removeEducationalProgram(educationalProgram.id);
},
  },
  created() {
    this.getEducationalPrograms(); 
    this.getFaculties();
  },
};
</script>