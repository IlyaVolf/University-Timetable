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
        <button type="button" class="btn btn-success btn-sm" v-b-modal.teacher-modal>Add Group</button>
        <button type="button" class="btn btn-success btn-sm" @click="yearShiftLeft()">Shift left</button>
        <button type="button" class="btn btn-success btn-sm" @click="yearShiftRight()">Shift right</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">SpecializationId</th>
              <th scope="col">Name</th>
              <th scope="col">amount of students</th>
              <th scope="col">Year of Study</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(group, index) in groups" :key="index">
              <!-- td : table data -->
              <td>{{group.specializationId}}</td>
              <td>{{group.name}}</td>
              <td>{{group.amountOfStudents}}</td>
              <td>{{group.yearOfStudy}}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.group-update-modal
                  @click="editGroup(group)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteGroup(group)">Delete</button>
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
    <b-modal ref="addGroupModal"
         id="group-modal"
         title="Add a new group" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-specializationId-group"
                  label="specializationId:"
                  label-for="form-specializationId-input">
      <b-form-input id="form-specializationId-input"
                    type="text"
                    v-model="addGroupForm.specializationId"
                    required
                    placeholder="Enter specializationId">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-name-group"
                  label="name:"
                  label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addGroupForm.name"
                        required
                        placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-amountOfStudents-group"
                  label="amountOfStudents:"
                  label-for="form-amountOfStudents-input">
          <b-form-input id="form-amountOfStudents-input"
                        type="text"
                        v-model="addGroupForm.amountOfStudents"
                        required
                        placeholder="Enter amountOfStudents">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-yearOfStudy-group"
                  label="yearOfStudy:"
                  label-for="form-yearOfStudy-input">
          <b-form-input id="form-yearOfStudy-input"
                        type="text"
                        v-model="addGroupForm.yearOfStudy"
                        required
                        placeholder="Enter yearOfStudy">
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editGroupModal"
         id="group-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-specializationId-edit-group"
                  label="specializationId:"
                  label-for="form-specializationId-edit-input">
        <b-form-input id="form-specializationId-edit-input"
                      type="text"
                      v-model="editForm.specializationId"
                      required
                      placeholder="Enter specializationId">
        </b-form-input>
  </b-form-group>

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

    
      
    <b-form-group id="form-amountOfStudents-edit-group"
                  label="amountOfStudents:"
                  label-for="form-amountOfStudents-edit-input">
        <b-form-input id="form-amountOfStudents-edit-input"
                      type="text"
                      v-model="editForm.amountOfStudents"
                      required
                      placeholder="Enter amountOfStudents">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-yearOfStudy-edit-group"
                  label="yearOfStudy:"
                  label-for="form-yearOfStudy-edit-input">
        <b-form-input id="form-yearOfStudy-edit-input"
                      type="text"
                      v-model="editForm.yearOfStudy"
                      required
                      placeholder="Enter yearOfStudy">
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
      groups: [],
      addGroupForm: {
        specializationId: '',
        name: '',
        amountOfStudents: '',
        yearOfStudy: '',
      },
      editForm: {
        id: '',
        specializationId: '',
        name: '',
        amountOfStudents: '',
        yearOfStudy: '',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getGroups() {
      const path = 'http://127.0.0.1:5000/groups';
      axios.get(path)
        .then((res) => {
          this.groups = res.data.groups;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 2 Add Faculty Button
    addGroup(payload) {
      const path = 'http://127.0.0.1:5000/groups';
      axios.post(path, payload)
        .then(() => {
          this.getGroups();
          
          // for message alert
          this.message = 'Faculty added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getGroups();
        });
    },
    yearShiftLeft(payload) {
      const path = 'http://localhost:5000/yearShiftLeft';
      axios.put(path, payload)
        .then(() => {
          this.getGroups();
          
          // for message alert
          this.message = 'Left shifted !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getGroups();
        });
    },
    yearShiftRight(payload) {
      const path = 'http://localhost:5000/yearShiftRight';
      axios.put(path, payload)
        .then(() => {
          this.getGroups();
          
          // for message alert
          this.message = 'Right shifted !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getGroups();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addGroupForm.specializationId = '';
        this.addGroupForm.name = '';
        this.addGroupForm.amountOfStudents = '';
        this.addGroupForm.yearOfStudy = '';
        this.editForm.id = '';
        this.editForm.specializationId = '';
        this.editForm.name = '';
        this.editForm.amountOfStudents = '';
        this.editForm.yearOfStudy = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGroupModal.hide();
      const payload = {
        specializationId: this.addGroupForm.specializationId,
        name: this.addGroupForm.name,
        amountOfStudents: this.addGroupForm.amountOfStudents,
        yearOfStudy: this.addGroupForm.yearOfStudy,
      };
      this.addGroup(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editGroupModal.hide();
    const payload = {
        specializationId: this.editForm.specializationId,
        name: this.editForm.name,
        amountOfStudents: this.editForm.amountOfStudents,
        yearOfStudy: this.editForm.yearOfStudy,
    };
    this.updateGroup(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addGroupModal.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
  updateGroup(id, payload) {
    const path = `http://127.0.0.1:5000/groups/${id}?specializationId=${payload.specializationId}&name=${payload.name}&amountOfStudents=${payload.amountOfStudents}&yearOfStudy=${payload.yearOfStudy}`;
    axios.put(path, payload, {
      
    })    
      .then(() => {
        this.getGroups();
        this.message = 'Information updated ⚙️!';
        this.showMessage =  true;
      })
      .catch((error) => {
        console.error(error);
        this.getGroups();
      });
  },
  // Handle Update Button 
  editGroup(group) {
    this.editForm = group;
  },
  // 5 Handle reset / cancel button click
  onResetUpdate(e) {
    e.preventDefault();
    this.$refs.editGroupModal.hide();
    this.initForm();
    this.getGroups(); 
  },
  // Remove teacher [ Delete Button ]
  removeGroup(id) {
    const path = `http://127.0.0.1:5000/groups/${id}`;
    axios.delete(path)
      .then(() => {
        this.getGroups();
        this.message = 'Info Removed 🗑️!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getGroups();
      });
  },
  // Handle Delete Button
  deleteGroup(group) {
    this.removeGroup(group.id);
  },
    },
    created() {
      this.getGroups(); 
    },
  };
</script>