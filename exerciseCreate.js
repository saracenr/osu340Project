window.onload = function() {
    document.getElementById("addMuscleGroup").addEventListener("click", function () {
        var element = document.createElement('div');
        var count = document.getElementById("muscleGroupContainer").childElementCount;
        element.id = 'chooseMuscleGroup' + count;
        element.innerHTML = `
            <label for="chooseMuscleGroup">Choose a muscle group!</label>
            <select>
            <option value="Arms">Arms</option>
            <option value="Chest">Chest</option>
            <option value="Shoulders">Shoulders</option>
            <option value="Upper back">Upper back</option>
            <option value="Lower back">Lower back</option>
        `;
        document.getElementById("muscleGroupContainer").appendChild(element);
    });

    document.getElementById("resetMuscleGroups").addEventListener("click", function () {
        element = document.getElementById("muscleGroupContainer");
        target = element.lastElementChild;
        element.removeChild(target);
    });
}
