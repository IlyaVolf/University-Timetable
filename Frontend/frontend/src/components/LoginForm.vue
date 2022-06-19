<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required
        ></b-form-input>
      </b-form-group>

    <b-form-group
		id="input-group-2" 
		label="Your Password:" 
		label-for="input-2"
		description=" Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.">
        <b-form-input 
			id="input-2"
			v-model="form.password"
			type = "text"
			placeholder="Enter password:"
			required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Log In</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';
  export default {
    data() {
      return {
        form: {
          email: '',
          password: '',
        },
		userRole: '',
        show: true
      }
    },
    methods: {
		sendLogin(payload) {
			const path = `http://127.0.0.1:5000/login?email=${payload.email}&password=${payload.password}`;
			axios.post(path, payload)
				.then(() => {
					console.log('Successful');

					this.getCurrentUser();
					window.location = 'http://127.0.0.1:8080';
				})
				.catch((error) => {
					if(error.response.data.error != null) {
						alert("Error: " + error.response.data.error)
						console.error(error);
					}
				});
		},
		getCurrentUser() {
			const path = 'http://127.0.0.1:5000/currentuser';
			axios.get(path)
			.then((res) => {
				console.log('Matvey');
				this.currentuser = res.data.currentuser;
				this.userRole = this.currentuser.role;
				console.log(res.data.currentuser);
			})
			.catch((error) => {
				console.log('Igorr');
				console.error(error);
		});
  },
    // 3 Submit form validator in the template @submit="onSubmit"  
      onSubmit(event) {
        event.preventDefault()
		const payload = {
			email: this.form.email,
			password: this.form.password
		};
		this.sendLogin(payload);
		//this.getCurrentUser();
        //alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.password = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>



<!--<template>
    <div class=e641_2070>
         <span  class="e641_2071">Вход</span>
         <div class=e641_2072>
            <span  class="e642_2097">Логин</span>
			<input  class="e642_2096">
         </div>
         <div class=e642_2098>
            <span  class="e642_2099">Пароль</span>
            <input type="password" class="e642_2100">
         </div>
         <button class=e641_2083><span  class="e641_2084">Продолжить</span></button>
      </div>
</template>

<style>
    .641_2070 { 
	overflow:hidden;
}
.e641_2070 { 
	box-shadow:0px 4px 4px rgba(222.4848711490631, 227.10773348808289, 234.81250405311584, 0.25);
	background-color:rgba(252.87500202655792, 252.87500202655792, 252.87500202655792, 1);
	width:466px;
	height:374px;
	border-top-left-radius:10px;
	border-top-right-radius:10px;
	border-bottom-left-radius:10px;
	border-bottom-right-radius:10px;
	position:absolute;
}
.e641_2071 { 
	color:rgba(36.00000165402889, 43.00000123679638, 53.00000064074993, 1);
	width:386px;
	height:36px;
	position:absolute;
	left:40px;
	top:40px;
	font-family:SF Pro Rounded;
	font-weight: bold;
	text-align:center;
	font-size:32px;
	letter-spacing:0;
	line-height:px;
}
.e641_2072 { 
	width:386px;
	height:77px;
	position:absolute;
	left:40px;
	top:96px;
}
.e642_2097 { 
	color:rgba(0, 0, 0, 1);
	width:43px;
	height:19px;
	position:absolute;
	left:0px;
	top:0px;
	font-family:SF Pro Display;
	text-align:left;
	font-size:16px;
	letter-spacing:0;
}
.e642_2096 { 
	background-color:rgba(237.4049985408783, 239.22186344861984, 242.24999696016312, 1);
	width:386px;
	height:48px;
	position:absolute;
	left:0px;
	top:29px;
	border-top-left-radius:12px;
	border-top-right-radius:12px;
	border-bottom-left-radius:12px;
	border-bottom-right-radius:12px;
}
.e642_2098 { 
	width:386px;
	height:77px;
	position:absolute;
	left:40px;
	top:193px;
}
.e642_2099 { 
	color:rgba(0, 0, 0, 1);
	width:52px;
	height:19px;
	position:absolute;
	left:0px;
	top:0px;
	font-family:SF Pro Display;
	text-align:left;
	font-size:16px;
	letter-spacing:0;
}
.e642_2100 { 
	background-color:rgba(237.4049985408783, 239.22186344861984, 242.24999696016312, 1);
	width:386px;
	height:48px;
	position:absolute;
	left:0px;
	top:29px;
	border-top-left-radius:12px;
	border-top-right-radius:12px;
	border-bottom-left-radius:12px;
	border-bottom-right-radius:12px;
}
.e641_2083 { 
	background-color:rgba(92.00000211596489, 197.0000034570694, 47.0000009983778, 1);
	width:386px;
	height:44px;
	position:absolute;
	left:40px;
	top:290px;
	border-top-left-radius:8px;
	border-top-right-radius:8px;
	border-bottom-left-radius:8px;
	border-bottom-right-radius:8px;
}
.e641_2084 { 
	color:rgba(255, 255, 255, 1);
	width:106px;
	height:20px;
	position:absolute;
	left:140px;
	top:12px;
	font-family:Inter;
	text-align:left;
	font-size:14px;
	letter-spacing:0;
	line-height:px;
}

</style>-->