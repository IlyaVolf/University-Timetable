<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/yeti/bootstrap.min.css"
      integrity="sha384-mLBxp+1RMvmQmXOjBzRjqqr0dP9VHU2tb3FK6VB0fJN/AOu7/y+CAeYeWJZ4b3ii" crossorigin="anonymous">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button"
              aria-controls="navbarSupportedContent"
              aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <b-collapse class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'schedule'}">
             Home
            </router-link>
          </li>
          <template v-if="userRole == 2">
            <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'TeacherConstraints'}">
             Teacher Constraints
            </router-link>
            </li>
          </template>
          <template v-if="userRole == 0 || userRole == 1">
            <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'FacultiesV'}">
             Faculties
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'TeachersV'}">
             Teachers
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'GroupsV'}">
             Groups
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'ClassroomsV'}">
             Classrooms
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'SubjectsV'}">
             Subjects
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'EducationalPrograms'}">
             Educational programs
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'SpecializationsV'}">
             Specializations
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'DispatcherTable'}">
             Dispatcher Table
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'UsersV'}">
             Users
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'ConstraintsV'}">
             Constraints
            </router-link>
          </li>
          </template>

        </ul>
        <ul class="navbar-nav">
          <template v-if="userRole == 3">
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'LoginForm'}">
              Login
              </router-link>
            </li>
          </template>
          <template v-if="userRole != 3">
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'LogOut'}">
              Logout
              </router-link>
            </li>
          </template>
        </ul>
      </b-collapse>
    </div>
    
  </nav>
  
</template>
<script>
import axios from 'axios';
export default {
  name: 'NavbarMain',
  data() {
    return {
      currentuser: [],
      userRole: [],
    };
  },
  message:'',
  methods: {
    // 1 GET METHOD
    getCurrentUser() {
    const path = 'http://127.0.0.1:5000/currentuser';
    axios.get(path)
    .then((res) => {
      this.currentuser = res.data.currentuser;
      this.userRole = this.currentuser.role;
      console.log(this.userRole);
    })
    .catch((error) => {
        console.error(error);
        if(error.response.status == 401) {
          window.location = 'http://127.0.0.1:8080/login';
        }
    });
  },
},
created() {
  this.getCurrentUser();
  },
}
</script>