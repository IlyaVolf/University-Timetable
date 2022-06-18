<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Users </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>Add User</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">Name</th>
              <th scope="col">Email</th>
             <!-- <th scope="col">Password hash</th>-->
              <th scope="col">Role</th>
              <th scope="col">TeacherId</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(user, index) in users" :key="index">
              <!-- td : table data -->
              
              <td>{{user.name}}</td>
              <td>{{user.email}}</td>
              <!--<td>{{user.passwordHash}}</td>-->
              <td>{{user.role}}</td>
              <td>{{user.teacherId}}</td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.user-update-modal
                  @click="editUser(user)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteUser(user)">Delete</button>
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
    <b-modal ref="addUserModal"
         id="user-modal"
         title="Add a new user" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">

    <b-form-group id="form-name-group"
                  label="name:"
                  label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addUserForm.name"
                        required
                        placeholder="Enter name">
        </b-form-input>
      </b-form-group>

    <b-form-group id="form-email-group"
                  label="email:"
                  label-for="form-email-input">
      <b-form-input id="form-email-input"
                    type="text"
                    v-model="addUserForm.email"
                    required
                    placeholder="Enter email">
      </b-form-input>
    </b-form-group>
      
    <b-form-group id="form-passwordHash-group"
                  label="passwordHash:"
                  label-for="form-passwordHash-input">
          <b-form-input id="form-passwordHash-input"
                        type="text"
                        v-model="addUserForm.passwordHash"
                        required
                        placeholder="Enter passwordHash">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-role-group"
                  label="role:"
                  label-for="form-role-input">
          <b-form-input id="form-role-input"
                        type="text"
                        v-model="addUserForm.role"
                        required
                        placeholder="Enter role">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-teacherId-group"
                  label="teacherId:"
                  label-for="form-teacherId-input">
          <b-form-input id="form-teacherId-input"
                        type="text"
                        v-model="addUserForm.teacherId"
                        required
                        placeholder="Enter teacherId">
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editUserModal"
         id="group-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-name-group"
                  label="name:"
                  label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter name">
        </b-form-input>
      </b-form-group>

    <b-form-group id="form-email-group"
                  label="email:"
                  label-for="form-email-input">
      <b-form-input id="form-email-input"
                    type="text"
                    v-model="editForm.email"
                    required
                    placeholder="Enter email">
      </b-form-input>
    </b-form-group>
      
    <b-form-group id="form-passwordHash-group"
                  label="passwordHash:"
                  label-for="form-passwordHash-input">
          <b-form-input id="form-passwordHash-input"
                        type="text"
                        v-model="editForm.passwordHash"
                        required
                        placeholder="Enter passwordHash">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-role-group"
                  label="role:"
                  label-for="form-role-input">
          <b-form-input id="form-role-input"
                        type="text"
                        v-model="editForm.role"
                        required
                        placeholder="Enter role">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-teacherId-group"
                  label="teacherId:"
                  label-for="form-teacherId-input">
          <b-form-input id="form-teacherId-input"
                        type="text"
                        v-model="editForm.teacherId"
                        required
                        placeholder="Enter teacherId">
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
      users: [],
      addUserForm: {
        name: '',
        email:'',
        passwordHash: '',
        role: '',
        teacherId: '',
      },
      editForm: {
        id: '',
        name: '',
        email:'',
        passwordHash: '',
        role: '',
        teacherId: '',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getUsers() {
      const path = 'http://127.0.0.1:5000/users';
      axios.get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 2 Add Faculty Button
    addUser(payload) {
      const path = 'http://127.0.0.1:5000/users?name=${payload.name}&email=${payload.email}&role=${payload.role}';
      axios.post(path, payload)
        .then(() => {
          this.getUsers();
          
          // for message alert
          this.message = 'User added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getUsers();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addUserForm.name = '';
        this.addUserForm.email = '';
        this.addUserForm.passwordHash = '';
        this.addUserForm.role = '';
        this.addUserForm.teacherId = '';
        this.editForm.id = '';
        this.editForm.name = '';
        this.editForm.email = '';
        this.editForm.passwordHash = '';
        this.editForm.role = '';
        this.editForm.teacherId = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addUserModal.hide();
      const payload = {
        name: this.addUserForm.name,
        email: this.addUserForm.name,
        passwordHash: this.addUserForm.passwordHash,
        role: this.addUserForm.role,
        teacherId:this.addUserForm.teacherId,
      };
      this.addUser(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editUserModal.hide();
    const payload = {
        sname: this.editForm.name,
        email: this.editForm.name,
        passwordHash: this.editForm.passwordHash,
        role: this.editForm.role,
        teacherId:this.editForm.teacherId,
    };
    this.updateUser(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
  updateUser(id, payload) {
    const path = `http://127.0.0.1:5000/users/${id}?name=${payload.name}&email=${payload.email}&role=${payload.role}`;
    axios.put(path, payload, {
      
    })    
      .then(() => {
        this.getUsers();
        this.message = 'Information updated ⚙️!';
        this.showMessage =  true;
      })
      .catch((error) => {
        console.error(error);
        this.getUserps();
      });
  },
  // Handle Update Button 
  editUser(user) {
    this.editForm = user;
  },
  // 5 Handle reset / cancel button click
  onResetUpdate(e) {
    e.preventDefault();
    this.$refs.editUserModal.hide();
    this.initForm();
    this.getUsers(); 
  },
  // Remove teacher [ Delete Button ]
  removeUser(id) {
    const path = `http://127.0.0.1:5000/users/${id}`;
    axios.delete(path)
      .then(() => {
        this.getUsers();
        this.message = 'Info Removed 🗑️!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getUsers();
      });
  },
  // Handle Delete Button
  deleteUser(user) {
    this.removeUser(user.id);
  },
    },
    created() {
      this.getUsers(); 
    },
  };
</script>