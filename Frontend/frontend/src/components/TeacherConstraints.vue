<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Teacher constraints </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Days can Work</th>
              <th scope="col">Days want Work</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr>
              <!-- td : table data -->
              <td>{{teacher.daysCanWork}}</td>
              <td>{{teacher.daysWantWork}}</td>
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
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        
        <!-- Footer -->
        <Footer class="bg-primary text-white text-center" style="border-radius:10px">Copyright &copy;. All Rights Reserved 2022.</Footer>

      </div>
    </div>
  <!-- Start of Modal 2 -->
  <b-modal ref="editTeacherModal"
         id="teacher-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">

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
        teacher: [],
        editForm: {
            id: '',
            daysCanWork: '',
            daysWantWork: '',
        },
        };
    },
    message:'',
    methods: {
        // 1 GET METHOD
        getTeachers() {
            const path = 'http://127.0.0.1:5000/teacherconstraints';
            axios.get(path)
                .then((res) => {
                this.teacher = res.data.teacher;
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
        // 5 initForm - add ediForm after the update method
        initForm() {
            this.editForm.id = '';
            this.editForm.daysCanWork = '';
            this.editForm.daysWantWork = '';
        }, 
        
    // MODAL 2
    // a- Handle the form Submit after updating
        onSubmitUpdate(e) {
            e.preventDefault();
            this.$refs.editTeacherModal.hide();
            const payload = {
                daysCanWork: this.editForm.daysCanWork,
                daysWantWork: this.editForm.daysWantWork,
            };
            this.updateTeacher(this.editForm.id, payload);
        },
    // 4 Update Alert Message 
    // Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
        updateTeacher(id, payload) {
        const path = `http://127.0.0.1:5000/teacherconstraints/?daysCanWork=${payload.daysCanWork}&daysWantWork=${payload.daysWantWork}`;
        axios.put(path, payload)    
            .then(() => {
            this.getTeachers();
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
    },
        created() {
            this.getTeachers(); 
        },
};
</script>