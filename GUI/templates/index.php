<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<style>
		.div1 {
			float: left;
			width: 30vw;
			height: 400px;
			display: inline-block;
			padding: 10px;
			border: 1px solid black;
			text-align: center;
			margin: auto;
		}
		.buttonBox {
			
			top: 390px;
		}
		.logo {
			white-space: nowrap;
			display: inline-block;
			position:fixed;
			top: 0;
			left: 0;
		}
		.label {
			color: white;
			padding: 5px;
		}
		
		</style>
	</head>
	<body>
		<div id="logo">
			<img src ="{{url_for('static', filename='oLabs.png')}}" width="600" height="100" />
			<h1 style="text-align:center;">Drone Classifier</h1>
		</div>
		<div style = "margin:auto;">
		<div class = "div1" style="background-image: url(../static/bossman1.png);background-size:100% 100%">
			<p>
			<span class="label">Number of Epochs: </span>
				<select name="epochs" id="epochs">
					<option value="1">1</option>
					<option value="10">10</option>
					<option value="15">15</option>
					<option value="20">20</option>
				</select>
			</p>
			<p></p>
			<span class="label">Validation Split: </span>
			<select name="split" id="split">
				<option value="0.2">20%</option> 
				<option value="0.30">30%</option> 
				<option value="0.35">35%</option> 
			</select>
			<br></br>
			<div class = "buttonBox">	
				<input type="button" onclick="'training()';" value="Start Training">
				<p id="text"></p>
			</div>
		</div>
		<div class = "div1" style="background-image: url(../static/bossman2.png);background-size:100% 100%">
			<div class = "buttonBox">	
				<input type="button" onclick="location.href='/inference';" value="Run Inference"/>
			</div>
		</div>
		<div class = "div1">
			<div class = "buttonBox">
				<p1>
				<img src="{{url_for('static', filename='foto00987_drone.jpg')}}" alt="Classified Drone" width="400" height="385" />
				</p1>
				<p2>
				<button onclick="location.href='results.html'">Show Results</button>
				</p2>
			</div>
		</div>
		</div>
		
		<script>	
			function training() {
				var e = document.getElementById("epochs").value;
				var split = document.getElementById("split").value; 
				var t = "/train/"+e+"/"+split
				document.getElementById("text").innerHTML = "Training Started";
				window.location.replace(t);
			}
		</script>		
	</body>
		

</html>
