**Pseudocode for thresholds used to trigger Alexa response**

Below is basic pseudocode that will take into account the data given in the data sets to determine when Alexa should be triggered to speak and with a ballpark response. Could also consider replacing if statements with while loops and add a cooldown timer between another Alexa trigger for the same response.

*Note:*

The code

 `timeOfDay > patientWakeUpTime AND timeOfDay < patientSleepTime`

would not be optimal for determining whether or not the patient is asleep or awake as anybody can stray away from their sleep schedules, this would be better implemented using other data given such as resting heart rate to determine whether or not the patient is asleep

**Lux Trigger**

if (lux <= 60 AND (timeOfDay > patientWakeUpTime AND timeOfDay < patientSleepTime)) {

Then triggerAlexa("It is dark in here, maybe you would feel more comfortable moving to a brighter location or perhaps turning on a light")

}

if (lux > 1000 AND patientLocation is inside) {

Then triggerAlexa("It is bright in here, maybe you would feel more comfortable moving to a less bright location or perhaps dimming the surrounding lighting")

}

if (luxFluctuating == true) {

Then triggerAlexa("The light levels here are unstable, you may feel more comfortable moving to another location")

}

**Heart Rate Trigger**

if (patientHeartRate > 100) {

Then triggerAlexa("Your heartrate is faster than normal, consider calming down to reduce this")

}

**Body Temperature Trigger**

if (patientBodyTemp > 37.5) {

Then triggerAlexa("Your core body temperature is increasing above normal levels, please ensure that you stay hydrated and take steps to cool down")

​	if (patientBodyTemp > 40) {

​	Then triggerAlexa("Your core body temperature has increased to dangerous levels, please seek assistance immediately")

​	}

}

if (patientBodyTemp < 35) {

Then triggerAlexa("Your core body temperature has fallen to a dangerous level, please take steps to warm up, if this is not possible, please seek assistance immediately")

}

**Location Temperature Trigger**

if (locationTemp > 21 AND (timeOfDay > patientWakeUpTime AND timeOfDay < patientSleepTime)) {

Then triggerAlexa("The room temperature may be increasing above comfortable levels, if so, stay hydrated and relocate to a cooler area")

}

if (locationTemp < 18 AND (timeOfDay > patientWakeUpTime AND timeOfDay < patientSleepTime)) {

Then triggerAlexa("The room temperature may be decreasing below comfortable levels, if so, remember to stay warm and relocate to a warmer area")

}

*Note:*

The next two statements would be used whilst the patient is asleep, and thus the Alexa response would be directed towards available staff or possibly to an automatic thermostat to control the temperature

if (locationTemp > 19 AND (timeOfDay < patientWakeUpTime AND timeOfDay > patientSleepTime)) {

Then triggerStaffAlexa("Patient's room temperature is above comfortable sleeping temperature, take measures to reduce temperature")

}

if (locationTemp < 15 AND (timeOfDay < patientWakeUpTime AND timeOfDay > patientSleepTime)) {

Then triggerStaffAlexa("Patient's room temperature is below comfortable sleeping temperature, take measures to increase temperature")

}

**References for Threshold Values:**

* [Chemocare.com](http://chemocare.com/chemotherapy/side-effects/rapid-heart-beat.aspx)
* [Disabled-World.com](https://www.disabled-world.com/calculators-charts/degrees.php)
* [BBC.com](https://www.bbc.com/news/magazine-12606943)
* [Tuck.com](https://www.tuck.com/best-temperature-for-sleep/)



