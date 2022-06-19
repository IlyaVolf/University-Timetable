import Vue from "vue";
import VueRouter from "vue-router";
import ScheduleHome from "../components/ScheduleHome.vue";
import FacultiesV from "../components/FacultiesV.vue";
import TeachersV from "../components/TeachersV.vue";
import GroupsV from "../components/GroupsV.vue";
import ClassroomsV from "../components/ClassroomsV.vue";
import ConstraintsV from "../components/ConstraintsV.vue";
//import TableOne from "../components/Tables/TableOne.vue";
import TableTwo from "../components/Tables/TableTwo.vue";
import EducationalPrograms from "../components/EducationalPrograms.vue";
import SpecializationsV from "../components/SpecializationsV.vue";
import LoginForm from "../components/LoginForm.vue";
import LogOut from "../components/LogOut.vue";
import UsersV from "../components/UsersV.vue"
import SubjectsV from "../components/SubjectsV.vue"
import DispatcherTable from "../components/DispatcherTable.vue"
import TeachersSchedule from "../components/schedule/TeachersSchedule.vue"
import TestV from "../components/TestV.vue"
import FacultiesSchedule from "../components/schedule/FacultiesSchedule.vue"
import GroupsForSchedule from "../components/schedule/GroupsForSchedule"

Vue.use(VueRouter);

/* eslint-disable */
const routes = [
  {
    path : '/testv',
    name : 'TestV',
    component : TestV, 
  },
  {
    path : '/logout',
    name : 'LogOut',
    component : LogOut, 
  },
  {
    path : '/schedule/teachers/:id',
    name : 'TeachersSchedule',
    component : TableTwo, 
  },
  {
    path : '/schedule/groups/:id',
    name : 'GroupsSchedule',
    component : TableTwo, 
  },
  {
    path : '/schedule/faculties/:id',
    name : 'GroupsForSchedule',
    component : GroupsForSchedule, 
  },
  {
    path : '/schedule/faculties',
    name : 'FacultiesSchedule',
    component : FacultiesSchedule, 
  },
  {
    path : '/schedule/teachers',
    name : 'TeachersSchedule',
    component : TeachersSchedule, 
  },
  {
    path : '/generatedClasses',
    name : 'DispatcherTable',
    component : DispatcherTable, 
  },
  {
    path : '/users',
    name : 'UsersV',
    component : UsersV, 
  },
  {
    path : '/subjects',
    name : 'SubjectsV',
    component : SubjectsV, 
  },
  {
    path : '/login',
    name : 'LoginForm',
    component : LoginForm, 
  },
  {
    path : '/faculties',
    name : 'FacultiesV',
    component : FacultiesV, 
  },
  {
    path : '/educationalPrograms',
    name : 'EducationalPrograms',
    component : EducationalPrograms, 
  },
  {
    path : '/specializations',
    name : 'SpecializationsV',
    component : SpecializationsV, 
  },
  {
    path : '/classrooms',
    name : 'ClassroomsV',
    component : ClassroomsV, 
  },
  {
    path : '/teachers',
    name : 'TeachersV',
    component : TeachersV, 
  },
  {
    path : '/timetable',
    name : 'TableTwo',
    component : TableTwo, 
  },
  {
    path : '/groups',
    name : 'GroupsV',
    component : GroupsV, 
  },
  {
    path : '/constraints',
    name : 'ConstraintsV',
    component : ConstraintsV, 
  },
  {
    path: '/',
    name: 'schedule',
    component: ScheduleHome,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
