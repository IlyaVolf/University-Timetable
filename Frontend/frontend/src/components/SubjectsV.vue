<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Subjects </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.teacher-modal>Add Subject</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
              <th scope="col">SpecializationId</th>
              <th scope="col">Name</th>
              <th scope="col">Semesters</th>
              <th scope="col">type of class</th>
              <th scope="col">frequency</th>
              <th scope="col">teacherId</th>
              <th scope="col">amount of groups</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr v-for="(subject, index) in subjects" :key="index">
              <!-- td : table data -->
              <td>{{subject.specializationId}}</td>
              <td>{{subject.name}}</td>
              <td>{{subject.semesters}}</td>
              <td>{{subject.typeOfClass}}</td>
              <td>{{subject.frequency}}</td>
              <td>{{subject.teacherId}}</td>
              <td>{{subject.amountOfGroups}}</td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.subject-update-modal
                  @click="editSubject(subject)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteSubject(subject)">Delete</button>
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
    <b-modal ref="addSubjectModal"
         id="subject-modal"
         title="Add a new subject" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-specializationId-subject"
                  label="specializationId:"
                  label-for="form-specializationId-input">
      <b-form-input id="form-specializationId-input"
                    type="text"
                    v-model="addSubjectForm.specializationId"
                    required
                    placeholder="Enter specializationId">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-name-subject"
                  label="name:"
                  label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addSubjectForm.name"
                        required
                        placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-semesters-subject"
                  label="semesters:"
                  label-for="form-semesters-input">
          <b-form-input id="form-semesters-input"
                        type="text"
                        v-model="addSubjectForm.semesters"
                        required
                        placeholder="Enter semesters">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-typeOfClass-subject"
                  label="typeOfClass:"
                  label-for="form-typeOfClass-input">
          <b-form-input id="form-typeOfClass-input"
                        type="text"
                        v-model="addSubjectForm.typeOfClass"
                        required
                        placeholder="Enter typeOfClass">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-frequency-subject"
                  label="frequency:"
                  label-for="form-frequency-input">
          <b-form-input id="form-frequency-input"
                        type="text"
                        v-model="addSubjectForm.frequency"
                        required
                        placeholder="Enter frequency">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-teacherId-subject"
                  label="teacherId:"
                  label-for="form-teacherId-input">
          <b-form-input id="form-teacherId-input"
                        type="text"
                        v-model="addSubjectForm.teacherId"
                        required
                        placeholder="Enter teacherId">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-amountOfGroups-subject"
                  label="amountOfGroups:"
                  label-for="form-amountOfGroups-input">
          <b-form-input id="form-amountOfGroups-input"
                        type="text"
                        v-model="addSubjectForm.amountOfGroups"
                        required
                        placeholder="Enter amountOfGroups">
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editSubjectModal"
         id="subject-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-specializationId-edit-subject"
                  label="specializationId:"
                  label-for="form-specializationId-edit-input">
        <b-form-input id="form-specializationId-edit-input"
                      type="text"
                      v-model="editForm.specializationId"
                      required
                      placeholder="Enter specializationId">
        </b-form-input>
  </b-form-group>

  <b-form-group id="form-name-edit-subject"
                label="Name:"
                label-for="form-name-edit-input">
      <b-form-input id="form-name-edit-input"
                    type="text"
                    v-model="editForm.name"
                    required
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>

    
      
    <b-form-group id="form-semesters-edit-subject"
                  label="semesters:"
                  label-for="form-semesters-edit-input">
          <b-form-input id="form-semesters-edit-input"
                        type="text"
                        v-model="editForm.semesters"
                        required
                        placeholder="Enter semesters">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-typeOfClass-edit-subject"
                  label="typeOfClass:"
                  label-for="form-typeOfClass-edit-input">
          <b-form-input id="form-typeOfClass-edit-input"
                        type="text"
                        v-model="editForm.typeOfClass"
                        required
                        placeholder="Enter typeOfClass">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-frequency-edit-subject"
                  label="frequency:"
                  label-for="form-frequency-edit-input">
          <b-form-input id="form-frequency-edit-input"
                        type="text"
                        v-model="editForm.frequency"
                        required
                        placeholder="Enter frequency">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-teacherId-edit-subject"
                  label="teacherId:"
                  label-for="form-teacherId-edit-input">
          <b-form-input id="form-teacherId-edit-input"
                        type="text"
                        v-model="editForm.teacherId"
                        required
                        placeholder="Enter teacherId">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-amountOfGroups-edit-subject"
                  label="amountOfGroups:"
                  label-for="form-amountOfGroups-edit-input">
          <b-form-input id="form-amountOfGroups-edit-input"
                        type="text"
                        v-model="editForm.amountOfGroups"
                        required
                        placeholder="Enter amountOfGroups">
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
      subjects: [],
      addSubjectForm: {
        specializationId: '',
        name: '',
        semesters:'',
        typeOfClass:'',
        frequency:'',
        teacherId:'',
        amountOfGroups: '',
      },
      editForm: {
        id:'',
        specializationId: '',
        name: '',
        semesters:'',
        typeOfClass:'',
        frequency:'',
        teacherId:'',
        amountOfGroups: '',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getSubjects() {
      const path = 'http://localhost:5000/subjects';
      axios.get(path)
        .then((res) => {
          this.subjects = res.data.subjects;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // 2 Add Faculty Button
    addSubjects(payload) {
      const path = 'http://localhost:5000/subjects';
      axios.post(path, payload)
        .then(() => {
          this.getSubjects();
          
          // for message alert
          this.message = 'Faculty added !';
          
          // to show message when faculty is added
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getSubjects();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addSubjectForm.specializationId = '';
        this.addSubjectForm.name = '';
        this.addSubjectForm.semesters = '';
        this.addSubjectForm.typeOfClass = '';
        this.addSubjectForm.frequency = '';
        this.addSubjectForm.teacherId = '';
        this.addSubjectForm.amountOfGroups = '';
        this.editForm.id = '';
        this.editForm.specializationId = '';
        this.editForm.name = '';
        this.editForm.semesters = '';
        this.editForm.typeOfClass = '';
        this.editForm.frequency = '';
        this.editForm.teacherId = '';
        this.editForm.amountOfGroups = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addSubjectsModal.hide();
      const payload = {
        specializationId: this.addSubjectForm.specializationId,
        name: this.addSubjectForm.name,
        semesters: this.addSubjectForm.semesters,
        typeOfClass: this.addSubjectForm.typeOfClass,
        frequency: this.addSubjectForm.frequency,
        teacherId: this.addSubjectForm.teacherId,
        amountOfGroups: this.addSubjectForm.amountOfGroups,
      };
      this.addSubjects(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editSubjectModal.hide();
    const payload = {
        specializationId: this.editForm.specializationId,
        name: this.editForm.name,
        semesters: this.editForm.semesters,
        typeOfClass: this.editForm.typeOfClass,
        frequency: this.editForm.frequency,
        teacherId: this.editForm.teacherId,
        amountOfGroups: this.editForm.amountOfGroups,
    };
    this.updateSubject(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addSubjectForm.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
  updateSubject(id, payload) {
    const path = `http://localhost:5000/subjects/${id}?specializationId=${payload.specializationId}&name=${payload.name}&semesters=${payload.semesters}&typeOfClass=${payload.typeOfClass}&frequency=${payload.frequency}&teacherId=${payload.teacherId}&amountOfGroups=${payload.amountOfGroups}`;
    axios.put(path, payload, {
      
    })    
      .then(() => {
        this.getSubjects();
        this.message = 'Information updated ⚙️!';
        this.showMessage =  true;
      })
      .catch((error) => {
        console.error(error);
        this.getSubjects();
      });
  },
  // Handle Update Button 
  editSubject(subject) {
    this.editForm = subject;
  },
  // 5 Handle reset / cancel button click
  onResetUpdate(e) {
    e.preventDefault();
    this.$refs.editSubjectModal.hide();
    this.initForm();
    this.getSubjects(); 
  },
  // Remove teacher [ Delete Button ]
  removeSubject(id) {
    const path = `http://localhost:5000/subjects/${id}`;
    axios.delete(path)
      .then(() => {
        this.getSubjects();
        this.message = 'Info Removed 🗑️!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getSubjects();
      });
  },
  // Handle Delete Button
  deletSubject(subject) {
    this.removeSubject(subject.id);
  },
    },
    created() {
      this.getSubjects(); 
    },
  };
</script>