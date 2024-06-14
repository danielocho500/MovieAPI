def get_cigar_description(cigar: int, reviews: int):
    if cigar == 0 and reviews == 0:
        return "No Reviews"
    elif cigar < 1:
        return "Sucks"
    elif cigar < 2:
        return "Watch Cars 2 and not waste your time"
    elif cigar < 3:
        return "Mehhh"
    elif cigar < 4:
        return "Nice, enjoy"
    else:
        return "En efecto, es cine..."