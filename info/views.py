from django.shortcuts import render


def index(request):
    universities = [
        {
            "name": "University of Cambridge",
            "courses": ["Medicine MB and BChir", "Engineering MEng"],
            "image": "kingscollege.png",
            "badge": {
                "text": "<span class='font-semibold'>New</span> Entrance Exams",
                "colour": "badge-green",
            },
        },
        {
            "name": "Imperial College London",
            "courses": [
                "Electronic and Electrical Engineering MEng",
                "Medicine MBBS",
                "BioChemistry MEng",
            ],
            "image": "imperialcollege.webp",
            "badge": {
                "text": "<span class='font-semibold'>New</span> Entrance Exams",
                "colour": "badge-green",
            },
        },
        {
            "name": "University College London",
            "courses": [
                "Mechanical Engineering MEng",
                "Chemistry MEng",
                "Electronic and Electrical Engineering MEng",
            ],
            "image": "ucl.png",
            "badge": {
                "text": "<span class='font-semibold'>New</span> Entrance Exams",
                "colour": "badge-green",
            },
        },
        {
            "name": "The University of Edinburgh",
            "courses": [
                "Electronics and Computer Science MEng",
                "Medicine MBBS",
                "Artificial Intelligence & Computer science BSc",
            ],
            "image": "uoe.png",
            "badge": {
                "text": "<span class='font-semibold'>Highly</span> Competitive",
                "colour": "bg-fuchsia-800",
            },
        },
        {
            "name": "The University of Manchester",
            "courses": [
                "Mathematics and Computer Science (with Industrial Placement) BSc",
                "Computer Science BSc",
            ],
            "image": "uom.png",
            "badge": {
                "text": "<span class='font-semibold'>Competitive</span> STEM",
                "colour": "bg-purple-800",
            },
        },
        {
            "name": "University of Warwick",
            "courses": [
                "Economics BSc",
                "Mechanical Engineering MEng",
                "Mathematics BSc",
                "Computer Science MEng",
            ],
            "image": "uow.png",
            "badge": {
                "text": "<span class='font-semibold'>World-class</span> Economics",
                "colour": "bg-rose-800",
            },
        },
    ]

    tutors = [
        {
            "name": "Viswa",
            "course": "Engineering",
            "university": "Imperial College London",
        }
    ] * 4
    return render(
        request, "info/index.html", context={"unis": universities, "tutors": tutors}
    )
