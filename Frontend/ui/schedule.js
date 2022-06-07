const schedule={template:`
<div>

<table class="table table-striped">
<thead>
    <tr>
        <th>
            Faculty
        </th>
        <th>
            Educational program
        </th>
        <th>
            Specialization
        </th>
        <th>
            Subject
        </th>
        <th>
            Semester
        </th>
        <th>
            Teacher
        </th>
        <th>
            TypeOfClass
        </th>
        <th>
            Auditory
        </th>
        <th>
            Groups
        </th>
        <th>
            Day
        </th>
        <th>
            ClassNumber
        </th>

    </tr>
</thead>
<tbody>
    <tr v-for="sch in schedules">
        <td>{{sch.Faculty}}</td>
        <td>{{sch.EducationalProgram}}</td>
        <td>{{sch.Specialization}}</td>
        <td>{{sch.Subject}}</td>
        <td>{{sch.Semester}}</td>
        <td>{{sch.Teacher}}</td>
        <td>{{sch.TypeOfClass}}</td>
        <td>{{sch.Auditory}}</td>
        <td>{{sch.Groups}}</td>
        <td>{{sch.Day}}</td>
        <td>{{sch.ClassNumber}}</td>
 
    </tr>
</tbody>
</thead>
</table>

</div>
`,

data(){
    return{
        schedules:[],
        modalTitle:"",
        Id:0,
        Faculty:"",
        EducationalProgram:"",
        Specialization:"",
        Subject:"",
        Semester:"",
        Teacher:"",
        Auditory:"",
        TypeOfClass:"",
        Groups:"",
        Day:"",
        ClassNumber:""
    }
},
methods:{
    refreshData(){
        axios.get(variables.API_URL+"gsch")
        .then((response)=>{
            this.schedules=response.data;
        });
    },
    
},

mounted:function(){
    this.refreshData();
}

}