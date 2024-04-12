function onPageLoad(){
  console.log("Getting categorical values...");
  // var url = "http://127.0.0.1:5000/get_categorical_values"; //If flask server runs localy.
  var url = "/api/get_categorical_values"; //If flask server runs online.
  $.get(url, function(data,status) {
      console.log("get response for categorical values");
      if(data){
          var brands_list = data.brand_name;
          for(var i in brands_list){
              var opt = new Option(brands_list[i]);
              $("#uibrand-menu").append(opt);
          }
        }
      }
  )
}
window.onload = onPageLoad;

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var brand_name = document.getElementById("uibrand-menu").value;
    console.log("Brand_name: " + brand_name);
    var ram = getRamValue();
    console.log("Ram: ",ram);
    var internal_memory = getInternalMemoryValue();
    console.log("Internal Memory: ", internal_memory);
    var cores = getCoresValue();
    console.log("Cores: ", cores)
    var rear_camera = document.getElementById("uiprimary_camera_rear").value;
    console.log("Rear Camera (MP): ", rear_camera)
    var front_camera = document.getElementById("uiprimary_camera_front").value;
    console.log("Front Camera (MP): ",     front_camera);
    var battery = document.getElementById("uiBattery").value;
    console.log("Battery (mAh): ", battery)
    var fast_charging = getFastChargingValue();
    console.log("Fast Charging: ", fast_charging);
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/get_estimated_price";
    // var url = "/api/get_estimated_price"
    $.post(url, {
      brand_name: brand_name,
      num_cores : cores,
      ram_capacity : ram,
      internal_memory : internal_memory,
      battery_capacity : battery,
      fast_charging_available : fast_charging,
      primary_camera_rear : rear_camera,
      primary_camera_front: front_camera
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " \u20ac</h2>";
      console.log(status);
  });
};


function getRamValue() {
    var uiram = document.getElementsByName("uiRam");
    for(var i in uiram) {
      if(uiram[i].checked) {
          return uiram[i].value;
      }
    }
    return -1; // Invalid Value
  }

  function getInternalMemoryValue() {
    var uistorage = document.getElementsByName("uiStorage");
    for(var i in uistorage) {
      if(uistorage[i].checked) {
          return uistorage[i].value;
      }
    }
    return -1; // Invalid Value
  }


  function getCoresValue() {
    var uicores = document.getElementsByName("uiCores");
    for(var i in uicores) {
      if(uicores[i].checked) {
          return uicores[i].value;
      }
    }
    return -1; // Invalid Value
  }

  function getFastChargingValue() {
    var uifastcharging = document.getElementsByName("uiFastcharging");
    for(var i in uifastcharging) {
      if(uifastcharging[i].checked) {
          return uifastcharging[i].value;
      }
    }
    return -1; // Invalid Value
  }