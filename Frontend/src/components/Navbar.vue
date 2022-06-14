<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button"
              :class="visible ? null : 'collapsed'"
              :aria-expanded="visible ? 'true' : 'false'"
              @click="visible = !visible"
              aria-controls="navbarSupportedContent"
              aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <b-collapse class="collapse navbar-collapse" id="navbarSupportedContent" v-model="visible">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'schedule'}" @click="visible = !visible">
             home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'FacultiesV'}" @click="visible = !visible">
             faculties
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'TeachersV'}" @click="visible = !visible">
             teachers
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'GroupsV'}" @click="visible = !visible">
             groups
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'ClassroomsV'}" @click="visible = !visible">
             classrooms
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'ConstraintsV'}" @click="visible = !visible">
             constraints
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'EducationalPrograms'}" @click="visible = !visible">
             Educational programs
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'SpecializationsV'}" @click="visible = !visible">
             Specializations
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{name: 'TableTwo'}" @click="visible = !visible">
             Table
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
};
</script>