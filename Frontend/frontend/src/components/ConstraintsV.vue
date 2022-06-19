<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <!-- Bootswatch -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
 <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css" integrity="sha384-HnTY+mLT0stQlOwD3wcAzSVAZbrBp141qwfR4WfTqVQKSgmcgzk+oP0ieIyrxiFO" crossorigin="anonymous"> -->

    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Constraints </h1>
        <hr><br>
        
         <!-- Alert -->
        <!-- Add Teacher button -->
        <button type="button" class="btn btn-success btn-sm" v-b-modal.constraint-modal>Add Constraint</button>
        <br><br>
        <!-- Add a bootstrap table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <!-- table header cells -->
                <th scope="col">First Class Starts</th>
                <th scope="col">Class Duration</th>
                <th scope="col">Short Break Duration</th>
                <th scope="col">Large Brake Duration</th>
                <th scope="col">Study Days in Week</th>
                <th scope="col">Study Days in Week for Students</th>
                <th scope="col">Classess per Day</th>
                <th scope="col">Classess per Day Students</th>
                <th scope="col">Classess per Day Teachers</th>
                <th scope="col">Lunch Brake</th>
                <th scope="col">Gaps</th>
                <th scope="col">Classroom Fillness</th>
                <th scope="col">Semester</th>
            </tr>
          </thead>
          <tbody>
            <!-- tr: table row -->
            <tr>
              <!-- td : table data -->
              <td>{{constraints.firstClassStarts}}</td>
              <td>{{constraints.classDuration}}</td>
              <td>{{constraints.shortBrakeDuration}}</td>
              <td>{{constraints.largeBrakeDuratiion}}</td>
              <td>{{constraints.studyDaysInWeek}}</td>
              <td>{{constraints.studyDaysInWeekForStudents}}</td>
              <td>{{constraints.studyDaysInWeekForTeachers}}</td>
              <td>{{constraints.classesPerDay}}</td>
              <td>{{constraints.classesPerDaySrudents}}</td>
              <td>{{constraints.classesPerDayTeachers}}</td>
              <td>{{constraints.lunchBrake}}</td>
              <td>{{constraints.gaps}}</td>
              <td>{{constraints.classroomFillness}}</td>
              <td>{{constraints.semester}}</td>
              <td>
                <div class="btn-group" role="group">
                   <!-- 2 Handle update button click -->
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.constraint-update-modal
                  @click="editConstraint(constraint)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteConstraint(constraint)">Delete</button>
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
    <b-modal ref="addConstraintModal"
         id="constraint-modal"
         title="Add a new constraint" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-firstClassStarts-constraint"
                  label="firstClassStarts:"
                  label-for="form-firstClassStarts-input">
      <b-form-input id="form-firstClassStarts-input"
                    type="text"
                    v-model="addConstraintForm.firstClassStarts"
                    required
                    placeholder="Enter firstClassStarts">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-classDuration-constraint"
                  label="classDuration:"
                  label-for="form-classDuration-input">
          <b-form-input id="form-classDuration-input"
                        type="text"
                        v-model="addConstraintForm.classDuration"
                        required
                        placeholder="Enter classDuration">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-shortBrakeDuration-constraint"
                  label="shortBrakeDuration:"
                  label-for="form-shortBrakeDuration-input">
          <b-form-input id="form-shortBrakeDuration-input"
                        type="text"
                        v-model="addConstraintForm.shortBrakeDuration"
                        required
                        placeholder="Enter shortBrakeDuration">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-largeBrakeDuration-constraint"
                  label="largeBrakeDuration:"
                  label-for="form-largeBrakeDuration-input">
          <b-form-input id="form-largeBrakeDuration-input"
                        type="text"
                        v-model="addConstraintForm.largeBrakeDuration"
                        required
                        placeholder="Enter largeBrakeDuration">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-studyDaysInWeek-constraint"
                  label="studyDaysInWeek:"
                  label-for="form-studyDaysInWeek-input">
          <b-form-input id="form-studyDaysInWeek-input"
                        type="text"
                        v-model="addConstraintForm.studyDaysInWeek"
                        required
                        placeholder="Enter studyDaysInWeek">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-studyDaysInWeekForStudents-constraint"
                  label="studyDaysInWeekForStudents:"
                  label-for="form-studyDaysInWeekForStudents-input">
          <b-form-input id="form-studyDaysInWeekForStudents-input"
                        type="text"
                        v-model="addConstraintForm.studyDaysInWeekForStudents"
                        required
                        placeholder="Enter studyDaysInWeekForStudents">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-studyDaysInWeekForTeachers-constraint"
                  label="studyDaysInWeekForTeachers:"
                  label-for="form-studyDaysInWeekForTeachers-input">
          <b-form-input id="form-studyDaysInWeekForTeachers-input"
                        type="text"
                        v-model="addConstraintForm.studyDaysInWeekForTeachers"
                        required
                        placeholder="Enter studyDaysInWeekForTeachers">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classesPerDay-constraint"
                  label="classesPerDay:"
                  label-for="form-classesPerDay-input">
          <b-form-input id="form-classesPerDay-input"
                        type="text"
                        v-model="addConstraintForm.classesPerDay"
                        required
                        placeholder="Enter classesPerDay">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classesPerDayStudents-constraint"
                  label="classesPerDayStudents:"
                  label-for="form-classesPerDayStudents-input">
          <b-form-input id="form-classesPerDayStudents-input"
                        type="text"
                        v-model="addConstraintForm.classesPerDayStudents"
                        required
                        placeholder="Enter classesPerDayStudents">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classesPerDayTeachers-constraint"
                  label="classesPerDayTeachers:"
                  label-for="form-classesPerDayTeachers-input">
          <b-form-input id="form-classesPerDayTeachers-input"
                        type="text"
                        v-model="addConstraintForm.classesPerDayTeachers"
                        required
                        placeholder="Enter classesPerDayTeachers">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-lunchBrake-constraint"
                  label="lunchBrake:"
                  label-for="form-lunchBrake-input">
          <b-form-input id="form-lunchBrake-input"
                        type="text"
                        v-model="addConstraintForm.lunchBrake"
                        required
                        placeholder="Enter lunchBrake">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-gaps-constraint"
                  label="gaps:"
                  label-for="form-gaps-input">
          <b-form-input id="form-gaps-input"
                        type="text"
                        v-model="addConstraintForm.gaps"
                        required
                        placeholder="Enter gaps">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classroomFillness-constraint"
                  label="classroomFillness:"
                  label-for="form-classroomFillness-input">
          <b-form-input id="form-classroomFillness-input"
                        type="text"
                        v-model="addConstraintForm.classroomFillness"
                        required
                        placeholder="Enter classroomFillness">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-semester-constraint"
                  label="semester:"
                  label-for="form-semester-input">
          <b-form-input id="form-semester-input"
                        type="text"
                        v-model="addConstraintForm.semester"
                        required
                        placeholder="Enter semester">
        </b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>
  <!-- End of modal 1 -->


  <!-- Start of Modal 2 -->
  <b-modal ref="editConstraintModal"
         id="constraint-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-firstClassStarts-edit-constraint"
                  label="firstClassStarts:"
                  label-for="form-firstClassStarts-edit-input">
        <b-form-input id="form-firstClassStarts-edit-input"
                      type="text"
                      v-model="editForm.firstClassStarts"
                      required
                      placeholder="Enter firstClassStarts">
        </b-form-input>
  </b-form-group>

  <b-form-group id="form-classDuration-edit-constraint"
                label="classDuration:"
                label-for="form-classDuration-edit-input">
      <b-form-input id="form-classDuration-edit-input"
                    type="text"
                    v-model="editForm.classDuration"
                    required
                    placeholder="Enter classDuration">
      </b-form-input>
    </b-form-group>

    
      
    <b-form-group id="form-shortBrakeDuration-edit-constraint"
                  label="shortBrakeDuration:"
                  label-for="form-shortBrakeDuration-edit-input">
          <b-form-input id="form-shortBrakeDuration-edit-input"
                        type="text"
                        v-model="editForm.shortBrakeDuration"
                        required
                        placeholder="Enter shortBrakeDuration">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-largeBrakeDuration-edit-constraint"
                  label="largeBrakeDuration:"
                  label-for="form-largeBrakeDuration-edit-input">
          <b-form-input id="form-largeBrakeDuration-edit-input"
                        type="text"
                        v-model="editForm.largeBrakeDuration"
                        required
                        placeholder="Enter largeBrakeDuration">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-studyDaysInWeek-edit-constraint"
                  label="studyDaysInWeek:"
                  label-for="form-studyDaysInWeek-edit-input">
          <b-form-input id="form-studyDaysInWeek-edit-input"
                        type="text"
                        v-model="editForm.studyDaysInWeek"
                        required
                        placeholder="Enter studyDaysInWeek">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-studyDaysInWeekForStudents-edit-constraint"
                  label="studyDaysInWeekForStudents:"
                  label-for="form-studyDaysInWeekForStudents-edit-input">
          <b-form-input id="form-studyDaysInWeekForStudents-edit-input"
                        type="text"
                        v-model="editForm.studyDaysInWeekForStudents"
                        required
                        placeholder="Enter studyDaysInWeekForStudents">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-studyDaysInWeekForTeachers-edit-constraint"
                  label="studyDaysInWeekForTeachers:"
                  label-for="form-studyDaysInWeekForTeachers-edit-input">
          <b-form-input id="form-studyDaysInWeekForTeachers-edit-input"
                        type="text"
                        v-model="editForm.studyDaysInWeekForTeachers"
                        required
                        placeholder="Enter studyDaysInWeekForTeachers">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classesPerDay-edit-constraint"
                  label="classesPerDay:"
                  label-for="form-classesPerDay-edit-input">
          <b-form-input id="form-classesPerDay-edit-input"
                        type="text"
                        v-model="editForm.classesPerDay"
                        required
                        placeholder="Enter classesPerDay">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classesPerDayStudents-edit-constraint"
                  label="classesPerDayStudents:"
                  label-for="form-classesPerDayStudents-edit-input">
          <b-form-input id="form-classesPerDayStudents-edit-input"
                        type="text"
                        v-model="editForm.classesPerDayStudents"
                        required
                        placeholder="Enter classesPerDayStudents">
        </b-form-input>
      </b-form-group>

    <b-form-group id="form-classesPerDayTeachers-edit-constraint"
                  label="classesPerDayTeachers:"
                  label-for="form-classesPerDayTeachers-edit-input">
          <b-form-input id="form-classesPerDayTeachers-edit-input"
                        type="text"
                        v-model="editForm.classesPerDayTeachers"
                        required
                        placeholder="Enter classesPerDayTeachers">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-lunchBrake-edit-constraint"
                  label="lunchBrake:"
                  label-for="form-lunchBrake-edit-input">
          <b-form-input id="form-lunchBrake-edit-input"
                        type="text"
                        v-model="editForm.lunchBrake"
                        required
                        placeholder="Enter lunchBrake">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-gaps-edit-constraint"
                  label="gaps:"
                  label-for="form-gaps-edit-input">
          <b-form-input id="form-gaps-edit-input"
                        type="text"
                        v-model="editForm.gaps"
                        required
                        placeholder="Enter gaps">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-classroomFillness-edit-constraint"
                  label="classroomFillness:"
                  label-for="form-classroomFillness-edit-input">
          <b-form-input id="form-classroomFillness-edit-input"
                        type="text"
                        v-model="editForm.classroomFillness"
                        required
                        placeholder="Enter classroomFillness">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-semester-edit-constraint"
                  label="semester:"
                  label-for="form-semester-edit-input">
          <b-form-input id="form-semester-edit-input"
                        type="text"
                        v-model="editForm.semester"
                        required
                        placeholder="Enter semester">
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
      constraints: [],
      addConstraintForm: {
        firstClassStarts: '',
        classDuration: '',
        shortBrakeDuration:'',
        largeBrakeDuration:'',
        studyDaysInWeek:'',
        studyDaysInWeekForStudents:'',
        studyDaysInWeekForTeachers: '',
        classesPerDay: '',
        classesPerDayStudents: '',
        classesPerDayTeachers: '',
        lunchBrake: '',
        gaps: '',
        classroomFillness: '',
        semester: '',
      },
      editForm: {
        id:'',
        firstClassStarts: '',
        classDuration: '',
        shortBrakeDuration:'',
        largeBrakeDuration:'',
        studyDaysInWeek:'',
        studyDaysInWeekForStudents:'',
        studyDaysInWeekForTeachers: '',
        classesPerDay: '',
        classesPerDayStudents: '',
        classesPerDayTeachers: '',
        lunchBrake: '',
        gaps: '',
        classroomFillness: '',
        semester: '',
      },
    };
  },
  message:'',
methods: {
    // 1 GET METHOD
    getConstraints() {
      const path = 'http://127.0.0.1:5000/constraints';
      axios.get(path)
        .then((res) => {
          this.constraints = res.data.constraints;
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
    // 2 Add Faculty Button
    addConstraints(payload) {
      const path = `http://127.0.0.1:5000/constraints?firstClassStarts=${payload.firstClassStarts}&classDuration=${payload.classDuration}&shortBrakeDuration=${payload.shortBrakeDuration}&largeBrakeDuration=${payload.largeBrakeDuration}&studyDaysInWeek=${payload.studyDaysInWeek}&studyDaysInWeekForStudents=${payload.studyDaysInWeekForStudents}&studyDaysInWeekForTeachers=${payload.studyDaysInWeekForTeachers}&classesPerDay=${payload.classesPerDay}&classesPerDayStudents=${payload.classesPerDayStudents}&classesPerDayTeachers=${payload.classesPerDayTeachers}&lunchBrake=${payload.lunchBrake}&gaps=${payload.gaps}&classroomFillness=${payload.classroomFillness}&semester=${payload.semester}`;
      axios.post(path, payload)
        .then(() => {
          this.getConstraints();
          
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
          this.getConstraints();
        });
    },
     // 5 initForm - add ediForm after the update method
     initForm() {
        this.addConstraintForm.firstClassStarts = '';
        this.addConstraintForm.classDuration = '';
        this.addConstraintForm.shortBrakeDuration = '';
        this.addConstraintForm.largeBrakeDuration = '';
        this.addConstraintForm.studyDaysInWeek = '';
        this.addConstraintForm.studyDaysInWeekForStudents = '';
        this.addConstraintForm.studyDaysInWeekForTeachers = '';
        this.addConstraintForm.classesPerDay = '';
        this.addConstraintForm.classesPerDayStudents = '';
        this.addConstraintForm.classesPerDayTeachers = '';
        this.addConstraintForm.lunchBrake = '';
        this.addConstraintForm.gaps = '';
        this.addConstraintForm.classroomFillness = '';
        this.addConstraintForm.semester = '';
        this.editForm.id = '';
        this.editForm.firstClassStarts = '';
        this.editForm.classDuration = '';
        this.editForm.shortBrakeDuration = '';
        this.editForm.largeBrakeDuration = '';
        this.editForm.studyDaysInWeek = '';
        this.editForm.studyDaysInWeekForStudents = '';
        this.editForm.studyDaysInWeekForTeachers = '';
        this.editForm.classesPerDay = '';
        this.editForm.classesPerDayStudents = '';
        this.editForm.classesPerDayTeachers = '';
        this.editForm.lunchBrake = '';
        this.editForm.gaps = '';
        this.editForm.classroomFillness = '';
        this.editForm.semester = '';
        
      }, 
    // 3 Submit form validator in the template @submit="onSubmit"  
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addConstraintModal.hide();
      const payload = {
        firstClassStarts: this.addConstraintForm.firstClassStarts,
        classDuration: this.addConstraintForm.classDuration,
        shortBrakeDuration: this.addConstraintForm.shortBrakeDuration,
        largeBrakeDuration: this.addConstraintForm.largeBrakeDuration,
        studyDaysInWeek: this.addConstraintForm.studyDaysInWeek,
        studyDaysInWeekForStudents: this.addConstraintForm.studyDaysInWeekForStudents,
        studyDaysInWeekForTeachers: this.addConstraintForm.studyDaysInWeekForTeachers,
        classesPerDay: this.addConstraintForm.classesPerDay,
        classesPerDayStudents: this.addConstraintForm.classesPerDayStudents,
        classesPerDayTeachers: this.addConstraintForm.classesPerDayTeachers,
        lunchBrake: this.addConstraintForm.lunchBrake,
        gaps: this.addConstraintForm.gaps,
        classroomFillness: this.addConstraintForm.classroomFillness,
        semester: this.addConstraintForm.semester,
      };
      this.addConstraints(payload);
      this.initForm();
    },
    
  // MODAL 2
  // a- Handle the form Submit after updating
    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editConstraintModal.hide();
    const payload = {
        firstClassStarts: this.editForm.firstClassStarts,
        classDuration: this.editForm.classDuration,
        shortBrakeDuration: this.editForm.shortBrakeDuration,
        largeBrakeDuration: this.editForm.largeBrakeDuration,
        studyDaysInWeek: this.editForm.studyDaysInWeek,
        studyDaysInWeekForStudents: this.editForm.studyDaysInWeekForStudents,
        studyDaysInWeekForTeachers: this.editForm.studyDaysInWeekForTeachers,
        classesPerDay: this.editForm.classesPerDay,
        classesPerDayStudents: this.editForm.classesPerDayStudents,
        classesPerDayTeachers: this.editForm.classesPerDayTeachers,
        lunchBrake: this.editForm.lunchBrake,
        gaps: this.editForm.gaps,
        classroomFillness: this.editForm.classroomFillness,
        semester: this.editForm.semester,
    };
    this.updateConstraint(this.editForm.id, payload);
  },
  // b- On reset method to reset items to default values
    onReset(e) {
      e.preventDefault();
      this.$refs.addConstraintForm.hide();
      this.initForm();
    },
// 4 Update Alert Message 
// Once the update is effective, we will get a message telling us that Teacher info Updated, and display the list of teachers after the update
  updateConstraint(id, payload) {
    const path = `http://127.0.0.1:5000/constraints/${id}?firstClassStarts=${payload.firstClassStarts}&classDuration=${payload.classDuration}&shortBrakeDuration=${payload.shortBrakeDuration}&largeBrakeDuration=${payload.largeBrakeDuration}&studyDaysInWeek=${payload.studyDaysInWeek}&studyDaysInWeekForStudents=${payload.studyDaysInWeekForStudents}&studyDaysInWeekForTeachers=${payload.studyDaysInWeekForTeachers}&classesPerDay=${payload.classesPerDay}&classesPerDayStudents=${payload.classesPerDayStudents}&classesPerDayTeachers=${payload.classesPerDayTeachers}&lunchBrake=${payload.lunchBrake}&gaps=${payload.gaps}&classroomFillness=${payload.classroomFillness}&semester=${payload.semester}`;
    axios.put(path, payload, {
      
    })    
      .then(() => {
        this.getConstraints();
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
        this.getConstraints();
      });
  },
  // Handle Update Button 
  editConstraint(constraint) {
    this.editForm = constraint;
  },
  // 5 Handle reset / cancel button click
  onResetUpdate(e) {
    e.preventDefault();
    this.$refs.editConstraintModal.hide();
    this.initForm();
    this.getConstraints(); 
  },
  // Remove teacher [ Delete Button ]
  removeConstraint(id) {
    const path = `http://127.0.0.1:5000/constraints/${id}`;
    axios.delete(path)
      .then(() => {
        this.getConstraints();
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
        this.getConstraints();
      });
  },
  // Handle Delete Button
  deleteConstraint(constraint) {
    this.removeConstraint(constraint.id);
  },
    },
    created() {
      this.getConstraints(); 
    },
  };
</script>
