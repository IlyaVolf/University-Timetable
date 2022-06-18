<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Classrooms </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.classroom-modal>Add Classroom</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Number</th>
              <th scope="col">Capacity</th>
              <th scope="col">Types of class</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(classroom, index) in classrooms" :key="index">
              <!-- td : table data -->
              <td>{{classroom.number}}</td>
              <td>{{classroom.capacity}}</td>
              <td>{{classroom.typesOfClass}}</td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.classroom-update-modal
                  @click="editClassroom(classroom)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteClassroom(classroom)">Delete</button>
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
    <b-modal ref="addClassroomModal"
         id="classroom-modal"
         title="Add a new classroom" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-number-classroom"
                  label="number:"
                  label-for="form-number-input">
      <b-form-input id="form-number-input"
                    type="text"
                    v-model="addClassroomForm.number"
                    required
                    placeholder="Enter number">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-capacity-classroom"
                  label="capacity:"
                  label-for="form-capacity-input">
          <b-form-input id="form-capacity-input"
                        type="text"
                        v-model="addClassroomForm.capacity"
                        required
                        placeholder="Enter capacity">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-typesOfClass-classroom"
                  label="typesOfClass:"
                  label-for="form-typesOfClass-input">
          <b-form-input id="form-typesOfClass-input"
                        type="text"
                        v-model="addClassroomForm.typesOfClass"
                        required
                        placeholder="Enter typesOfClass">
        </b-form-input>
      </b-form-group>


      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editClassroomModal"
         id="classroom-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-number-edit-classroom"
                  label="number:"
                  label-for="form-number-edit-input">
        <b-form-input id="form-number-edit-input"
                      type="text"
                      v-model="editForm.number"
                      required
                      placeholder="Enter number">
        </b-form-input>
  </b-form-group>

  <b-form-group id="form-capacity-edit-classroom"
                label="capacity:"
                label-for="form-capacity-edit-input">
      <b-form-input id="form-capacity-edit-input"
                    type="text"
                    v-model="editForm.capacity"
                    required
                    placeholder="Enter capacity">
      </b-form-input>
    </b-form-group>

    
      
    <b-form-group id="form-typesOfClass-edit-classroom"
                  label="typesOfClass:"
                  label-for="form-typesOfClass-edit-input">
          <b-form-input id="form-typesOfClass-edit-input"
                        type="text"
                        v-model="editForm.typesOfClass"
                        required
                        placeholder="Enter typesOfClass">
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
      classrooms: [],
      addClassroomForm: {
        number: '',
        capacity: '',
        typesOfClass:'',
      },
      editForm: {
        id:'',
        number: '',
        capacity: '',
        typesOfClass:'',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getClassrooms() {
      const path = 'http://localhost:5000/classrooms';
      axios.get(path)
        .then((res) => {
          this.classrooms = res.data.classrooms;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 2 Add Faculty Button
    addClassroom(payload) {
      const path = `http://localhost:5000/classrooms?number=${payload.number}&capacity=${payload.capacity}&typesOfClass=${payload.typesOfClass}`;
      axios.post(path, payload)
        .then(() => {
          this.getClassrooms();
          
          // for message alert
          this.message = 'Classroom added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getClassrooms();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addClassroomForm.number = '';
        this.addClassroomForm.capacity = '';
        this.addClassroomForm.typesOfClass = '';
        this.editForm.id = '';
        this.editForm.number = '';
        this.editForm.capacity = '';
        this.editForm.typesOfClass = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addClassroomModal.hide();
      const payload = {
        number: this.addClassroomForm.number,
        capacity: this.addClassroomForm.capacity,
        typesOfClass: this.addClassroomForm.typesOfClass,
      };
      this.addClassroom(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editClassroomModal.hide();
    const payload = {
        number: this.editForm.number,
        capacity: this.editForm.capacity,
        typesOfClass: this.editForm.typesOfClass,
    };
    this.updateClassroom(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addClassroomForm.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
  updateClassroom(id, payload) {
    const path = `http://localhost:5000/classrooms/${id}?number=${payload.number}&capacity=${payload.capacity}&typesOfClass=${payload.typesOfClass}`;
    axios.put(path, payload, {
      
    })    
      .then(() => {
        this.getClassrooms();
        this.message = 'Information updated ⚙️!';
        this.showMessage =  true;
      })
      .catch((error) => {
        console.error(error);
        this.getClassrooms();
      });
  },
  // Handle Update Button 
  editClassroom(classroom) {
    this.editForm = classroom;
  },
  // 5 Handle reset / cancel button click
  onResetUpdate(e) {
    e.preventDefault();
    this.$refs.editClassroomModal.hide();
    this.initForm();
    this.getClassrooms(); 
  },
  // Remove teacher [ Delete Button ]
  removeClassroom(id) {
    const path = `http://localhost:5000/classrooms/${id}`;
    axios.delete(path)
      .then(() => {
        this.getClassrooms();
        this.message = 'Info Removed 🗑️!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getClassrooms();
      });
  },
  // Handle Delete Button
  deleteClassroom(classroom) {
    this.removeClassroom(classroom.id);
  },
    },
    created() {
      this.getClassrooms(); 
    },
  };
</script>