#file containing all functions that are suceptible to be integrated and reused 

#returns the tier number of the teacher in the textgrid file from pyannote 
#if there is no teacher returns -1
def teacher_nb(name_of_file):
    
    txtGrid_file = open(name_of_file, "r") #open the textgrid file
    intervals_list = [] #list that contain the number of intervals for each tier

    #we loop on the txtGrid_file 
    for line in txtGrid_file:

        if line.startswith("size = "):
            #we get the number of speakers in the audio file
            nb_speaker = int(line[7:])
            if nb_speaker <= 2:
                #there is no teacher
                return -1
        elif line.startswith("            intervals: size = "):
            #get the number of intervals for this tier
            intervals_list.append(int(line[30:]))

    index = 0
    index_min = 0
    min = 0
    for size in intervals_list:
        #we loop on the intervals_list to find the indx for which the size is the smallest
        if size < min  :
            min = size
            index_min = index
        index += 1

    return index_min

#function that returns a bool stating the order of the speaker in the audio file (using the textgrid file drom pyannote)
#true if in the normal order false if in the reverse order
def is_speaker_order_normal(name_of_file):

    txtGrid_file = open(name_of_file, "r") #open the textgrid file

    get_time = False  #boolean to know if we have to get the time or not (depends if we are in the right segment or not)
    teacher_tier = teacher_nb(name_of_file) #get the tier number of the teacher
    speaker_list = [0,0,0]  #list that will contain the min speaking time for each speaker 

    #loop over the textgrid file to get two times where the speakers speak first
    for line in txtGrid_file:
        if line.startswith("    item ["):
            #we are at the beginning of a tier, we can get the time the next time the speaker speaks
            get_time = True   
            tier = int(line[10])     #we get the tier to verify that we do not take into account the teacher 
        elif line.startswith("                xmin = ") : 
            xmin = float(line[23:])
        elif line.startswith("                text = \"SPEAKER_"):
            if get_time and tier != teacher_tier:
                #we are in the right segment, we can get the time
                speaker_nb = int(line[32:34])
                speaker_list[speaker_nb] = xmin
                get_time = False

    #we compare the two times to know if the speakers are in the normal order or not
    teacher_snb = speaker_list.index(0)
    if teacher_snb == 0:
        return speaker_list[1] <= speaker_list[2]
    if teacher_snb == 1:
        return speaker_list[0] <= speaker_list[2]
    if teacher_snb == 2:
        return speaker_list[0] <= speaker_list[1]
