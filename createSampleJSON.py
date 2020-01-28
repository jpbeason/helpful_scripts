import json
import copy

"""
Update below template object to your desired schema.

"""

templateObject = {}
templateObject["image"] = "https://dummyimage.com/200x200/000000/0011ff.png"
templateObject["description"] = "This is a placeholder for the project's description."
templateObject["category"] = "Category Name"
templateObject["year"] = "2020"
templateObject["status"] = "In Progress"
templateObject["members"] = "Member #1, Member #2, Member #3, Member #4"
templateObject["link"] = "https://www.optimizemi.org/"

values = {}
sampleData = []


# TO DO: manipulate iteratively as desired
for i in range(15):
	idNum = str(i)

    # TO DO: manipulate iteratively as desired
    values = copy.deepcopy(templateObject)
    title = "Project Title #" + idNum
    values["title"] = title

    sampleData.append(values)

# TO DO: specify output file
fout = open("placeholderProjectData.json", "w+")
fout.write(json.dumps(sampleData, indent=4))
