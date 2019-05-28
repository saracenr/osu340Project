window.onload = function() {
    document.getElementById("addMuscleGroup").addEventListener("click", function () {
        var element = document.createElement('input');
        var count = document.getElementById("muscleGroupContainer").childElementCount;
        var selectionElement = document.getElementById('muscleGroupSelection');
        var selection = selectionElement.options[selectionElement.selectedIndex].value;
        element.id = 'chooseMuscleGroup' + count;
        element.name = 'muscleGroups';
        element.textContent = selection
        element.innerHTML = `
            <div>` + selection + `</div>
        `;
        document.getElementById("muscleGroupContainer").appendChild(element);
    });

    document.getElementById("removeMuscleGroup").addEventListener("click", function () {
        element = document.getElementById("muscleGroupContainer");
        target = element.lastElementChild;
        element.removeChild(target);
    });
}
