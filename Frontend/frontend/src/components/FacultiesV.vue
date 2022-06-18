<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Faculties </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.faculty-modal>Add Faculty</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Faculty</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(faculty, index) in faculties" :key="index">
              <!-- td : table data -->
              <td>{{faculty.faculty}}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.faculty-update-modal
                  @click="editFaculty(faculty)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteFaculty(faculty)">Delete</button>
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
    <b-modal ref="addFacultyModal"
         id="faculty-modal"
         title="Add a new faculty" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-faculty-group"
                  label="Faculty:"
                  label-for="form-faculty-input">
      <b-form-input id="form-faculty-input"
                    type="text"
                    v-model="addFacultyForm.faculty"
                    required
                    placeholder="Enter faculty">
      </b-form-input>
    </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editFacultyModal"
         id="faculty-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-faculty-edit-group"
                label="Faculty:"
                label-for="form-faculty-edit-input">
      <b-form-input id="form-faculty-edit-input"
                    type="text"
                    v-model="editForm.faculty"
                    required
                    placeholder="Enter faculty">
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
      faculties: [],
      addFacultyForm: {
        faculty: '',
      },
      editForm: {
        id: '',
        faculty: '',
      },
    };
  },
  message:'',
methods: {
  //getCurrentUser(){
      //return currnetuser
  //for dispatchers if (currentuser.role == 0 or 1) {
    //error('No access')
  //}
  //only for teachers if(currnetuser.role == 2)
  //error('No access')

    // 1 GET METHOD
    getFaculties() {
      const path = 'http://localhost:5000/faculties';
      axios.get(path)
        .then((res) => {
          this.faculties = res.data.faculties;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    
    // 2 Add Faculty Button
    addFaculty(payload) {
      const path = `http://localhost:5000/faculties?name=${payload.faculty}`;
      axios.post(path, payload)
        .then(() => {
          this.getFaculties();
          
          // for message alert
          this.message = 'Faculty added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getFaculties();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addFacultyForm.faculty = '';
        this.editForm.id = '';
        this.editForm.faculty = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addFacultyModal.hide();
      const payload = {
        faculty: this.addFacultyForm.faculty,
      };
      this.addFaculty(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editFacultyModal.hide();
    const payload = {
      faculty: this.editForm.faculty,
    };
    this.updateFaculty(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addFacultyModal.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
  updateFaculty(id, payload) {
    const path = `http://localhost:5000/faculties/${id}?name=${payload.faculty}`;
    axios.put(path, payload, {
      
    })    
      .then(() => {
        this.getFaculties();
        this.message = 'Information updated ⚙️!';
        this.showMessage =  true;
      })
      .catch((error) => {
        console.error(error);
        this.getFaculties();
      });
  },
  // Handle Update Button 
  editFaculty(faculty) {
    this.editForm = faculty;
  },
  // 5 Handle reset / cancel button click
  onResetUpdate(e) {
    e.preventDefault();
    this.$refs.editFacultyModal.hide();
    this.initForm();
    this.getFaculties(); 
  },
  // Remove teacher [ Delete Button ]
  removeFaculty(id) {
    const path = `http://localhost:5000/faculties/${id}`;
    axios.delete(path)
      .then(() => {
        this.getFaculties();
        this.message = 'Info Removed 🗑️!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getFaculties();
      });
  },
  // Handle Delete Button
  deleteFaculty(faculty) {
    this.removeFaculty(faculty.id);
  },
    },
    created() {
      this.getFaculties(); 
    },
  };
</script>