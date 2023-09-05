<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Specializations </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.specialization-modal>Add Specialization</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Educational Program</th>
              <th scope="col">Name</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(specialization, index) in specializations" :key="index">
              <!-- td : table data -->
              <td>{{specialization.educationalProgram}}</td>
              <td>{{specialization.specialization}}</td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.specialization-update-modal
                  @click="editSpecialization(specialization)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteSpecialization(specialization)">Delete</button>
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
    <b-modal ref="addSpecializationModal"
         id="specialization-modal"
         title="Add a new specialization" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-educationalProgramId-group"
                  label="EducationalProgramId:"
                  label-for="form-educationalProgram-input">
                  
         <b-form-input
          id="form-educationalProgramId-input"
          v-model="addSpecializationForm.educationalProgramId"
          required
        ></b-form-input>
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

    <b-form-group id="form-specialization-specialization"
                  label="specialization:"
                  label-for="form-specialization-input">
                  
      <b-form-input id="form-specialization-input"
                    type="text"
                    v-model="addSpecializationForm.name"
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
  <b-modal ref="editSpecializationModal"
         id="specialization-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-educationalProgramId-edit-group"
                label="educationalProgramId:"
                label-for="form-educationalProgramId-edit-input">
      <b-form-input id="form-educationalProgramId-edit-input"
                    type="text"
                    v-model="editForm.educationalProgramId"
                    required
                    placeholder="Enter educationalProgramId">
                   
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-specialization-edit-specialization"
                label="Name:"
                label-for="form-specialization-edit-input">
      <b-form-input id="form-specialization-edit-input"
                    type="text"
                    v-model="editForm.specialization"
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
      specializations:[],
      educationalPrograms: [],
      addSpecializationForm: {
        educationalProgramId: '',
        specialization: '',
      },
      editForm: {
        id: '',
        educationalProgramId: '',
        specialization: '',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getSpecializations() {
      const path = 'http://127.0.0.1:5000/specializations';
      axios.get(path)
        .then((res) => {
          this.specializations = res.data.specializations;
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
    // 2 Add Teacher Button
    addSpecialization(payload) {
      const path = `http://127.0.0.1:5000/specializations?educationalProgramId=${payload.educationalProgramId}&name=${payload.name}`;
      axios.post(path, payload)
        .then(() => {
          this.getSpecializations();
          
          // for message alert
          this.message = 'Specialization added !';
          
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
          this.getSpecializations();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addSpecialization.educationalProgramId = '';
        this.addSpecialization.name = '';
        this.editForm.id = '';
        this.editForm.educationalProgramId = '';
        this.editForm.name = '';
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addSpecializationModal.hide();
      const payload = {
        educationalProgramId: this.addSpecializationForm.educationalProgramId,
        name: this.addSpecializationForm.name,
      };
      this.addSpecialization(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editSpecializationModal.hide();
    const payload = {
      educationalProgramId: this.addSpecializationForm.educationalProgramId,
      name: this.addSpecializationForm.name,
    };
    this.updateSpecialization(payload, this.editForm.id);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addSpecializationModal.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
updateSpecialization(payload, id) {
  const path = `http://127.0.0.1:5000/specializations/${id}?educationalProgramId=${payload.educationalProgramId}&name=${payload.name}`;
  axios.put(path, payload)    
    .then(() => {
      this.getSpecializations();
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
      this.getSpecializations();
    });
},
 // Handle Update Button 
editSpecialization(specialization) {
  this.editForm = specialization;
},
// 5 Handle reset / cancel button click
onResetUpdate(e) {
  e.preventDefault();
  this.$refs.editSpecializationModal.hide();
  this.initForm();
  this.getSpecializations(); 
},
// Remove teacher [ Delete Button ]
removeSpecialization(id) {
  const path = `http://127.0.0.1:5000/specializations/${id}`;
  axios.delete(path)
    .then(() => {
      this.getSpecializations();
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
      this.getSpecializations();
    });
},
// Handle Delete Button
deleteSpecialization(specialization) {
  this.removeSpecialization(specialization.id);
},
  },
  created() {
    this.getSpecializations(); 
  },
};
</script>