<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Teachers </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.teacher-modal>Add Teacher</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Name</th>
              <th scope="col">Days can Work</th>
              <th scope="col">Days want Work</th>
              <th scope="col">Weight</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(teacher, index) in teachers" :key="index">
              <!-- td : table data -->
              <td>{{teacher.name}}</td>
              <td>{{teacher.daysCanWork}}</td>
              <td>{{teacher.daysWantWork}}</td>
              <td>{{teacher.weight}}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.teacher-update-modal
                  @click="editTeacher(teacher)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteTeacher(teacher)">Delete</button>
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
    <b-modal ref="addTeacherModal"
         id="teacher-modal"
         title="Add a new teacher" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-name-group"
                  label="Name:"
                  label-for="form-name-input">
      <b-form-input id="form-name-input"
                    type="text"
                    v-model="addTeacherForm.name"
                    required
                    placeholder="Enter Name">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-daysCanWork-group"
                  label="DaysCanWork:"
                  label-for="form-daysCanWork-input">
          <b-form-input id="form-daysCanWork-input"
                        type="text"
                        v-model="addTeacherForm.daysCanWork"
                        required
                        placeholder="Enter daysCanWork">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-daysWantWork-group"
                  label="DaysWantWork:"
                  label-for="form-daysWantWork-input">
          <b-form-input id="form-daysWantWork-input"
                        type="text"
                        v-model="addTeacherForm.daysWantWork"
                        required
                        placeholder="Enter daysWantWork">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-weight-group"
                  label="Weight:"
                  label-for="form-weight-input">
          <b-form-input id="form-weight-input"
                        type="text"
                        v-model="addTeacherForm.weight"
                        required
                        placeholder="Enter weight">
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editTeacherModal"
         id="teacher-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-name-edit-group"
                label="Name:"
                label-for="form-name-edit-input">
      <b-form-input id="form-name-edit-input"
                    type="text"
                    v-model="editForm.name"
                    required
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-daysCanWork-edit-group"
                  label="DaysCanWork:"
                  label-for="form-daysCanWork-edit-input">
        <b-form-input id="form-daysCanWork-edit-input"
                      type="text"
                      v-model="editForm.daysCanWork"
                      required
                      placeholder="Enter daysCanWork">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-daysWantWork-edit-group"
                  label="DaysWantWork:"
                  label-for="form-daysWantWork-edit-input">
        <b-form-input id="form-daysWantWork-edit-input"
                      type="text"
                      v-model="editForm.daysWantWork"
                      required
                      placeholder="Enter daysWantWork">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-weight-edit-group"
                  label="Weight:"
                  label-for="form-weight-edit-input">
        <b-form-input id="form-weight-edit-input"
                      type="text"
                      v-model="editForm.weight"
                      required
                      placeholder="Enter weight">
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
      teachers: [],
      addTeacherForm: {
        name: '',
        daysCanWork: '',
        daysWantWork: '',
        weight: '',
      },
      editForm: {
        id: '',
        name: '',
        daysCanWork: '',
        daysWantWork: '',
        weight: '',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getTeachers() {
      const path = 'http://127.0.0.1:5000/teachers';
      axios.get(path)
        .then((res) => {
          this.teachers = res.data.teachers;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 2 Add Teacher Button
    addTeacher(payload) {
      const path = 'http://127.0.0.1:5000/teachers/';
      axios.post(path, payload)
        .then(() => {
          this.getTeachers();
          
          // for message alert
          this.message = 'Teachers added !';
          
          // to show message when teacher is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getTeachers();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addTeacherForm.name = '';
        this.addTeacherForm.daysCanWork = '';
        this.addTeacherForm.daysWantWork = '';
        this.addTeacherForm.weight = '';
        this.editForm.id = '';
        this.editForm.name = '';
        this.editForm.daysCanWork = '';
        this.editForm.daysWantWork = '';
        this.editForm.weight = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addTeacherModal.hide();
      const payload = {
        name: this.addTeacherForm.name,
        daysCanWork: this.addTeacherForm.daysCanWork,
        daysWantWork: this.addTeacherForm.daysWantWork,
        weight: this.addTeacherForm.weight,
      };
      this.addTeacher(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editTeacherModal.hide();
    const payload = {
      name: this.editForm.name,
        daysCanWork: this.editForm.daysCanWork,
        daysWantWork: this.editForm.daysWantWork,
        weight: this.editForm.weight,
    };
    this.updateTeacher(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addTeacherModal.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
updateTeacher(id, payload) {
  const path = `http://127.0.0.1:5000/teachers/${id}?name=${payload.name}&daysCanWork=${payload.daysCanWork}&daysWantWork=${payload.daysWantWork}&weight=${payload.weight}`;
  axios.put(path, payload)    
    .then(() => {
      this.getTeachers();
      this.message = 'Information updated ⚙️!';
      this.showMessage =  true;
    })
    .catch((error) => {
      console.error(error);
      this.getTeachers();
    });
},
 // Handle Update Button 
editTeacher(teacher) {
  this.editForm = teacher;
},
// 5 Handle reset / cancel button click
onResetUpdate(e) {
  e.preventDefault();
  this.$refs.editTeacherModal.hide();
  this.initForm();
  this.getTeachers(); 
},
// Remove teacher [ Delete Button ]
removeTeacher(id) {
  const path = `http://127.0.0.1:5000/teachers/${id}`;
  axios.delete(path)
    .then(() => {
      this.getTeachers();
      this.message = 'Info Removed 🗑️!';
      this.showMessage = true;
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
      this.getTeachers();
    });
},
// Handle Delete Button
deleteTeacher(teacher) {
  this.removeTeacher(teacher.id);
},
  },
  created() {
    this.getTeachers(); 
  },
};
</script>