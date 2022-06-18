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
             home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'FacultiesV'}">
             faculties
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'TeachersV'}">
             teachers
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'GroupsV'}">
             groups
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'ClassroomsV'}">
             classrooms
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'SubjectsV'}">
             Subjects
            </router-link>
          </li>
          <!--
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'ConstraintsV'}">
             constraints
            </router-link>
          </li>-->
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
            <router-link class="nav-link" :to="{name: 'TableTwo'}">
             Table
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
          
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" :to="{name: 'LoginForm'}">
              Login
              </router-link>
            </li>
        </ul>
      </b-collapse>
    </div>
    
  </nav>
  
</template>
<script>
export default {
  name: 'NavbarMain'
}
</script>