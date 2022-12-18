'''
1) Husband [AnNisa 4:12]
   a. Gets 1/2
      i. Deceased does not have any offspring
   b. Gets 1/4
      i. Deceased has offspring
'''
def husband_inheritance(has_offspring):
    if has_offspring:
        return 0.25
    else:
        return 0.5
'''
2) Wife (Divided equally among all wives) [AnNisa 4:12]
   a. Gets 1/4
      i. Deceased does not have any offspring
   b. Gets 1/8
      i. Deceased has offspring
'''
def wife_inheritance(has_offspring):
    if has_offspring:
        return 0.125
    else:
        return 0.25
'''
3) Daughter (Divided equally among all daughters)
   a. Gets 1/2 [AnNisa 4:11]
      i. Deceased has only 1 daughter, and [AnNisa 4:11]
      ii. Deceased does not have any sons [AnNisa 4:11]
   b. Gets 2/3 [AnNisa 4:11]
      i. Deceased has multiple daughters, and [AnNisa 4:11]
      ii. Deceased does not have any sons [AnNisa 4:11]
'''
def daughter_inheritance(num_daughters, has_sons):
    if num_daughters == 1 and not has_sons:
        return 0.5
    elif num_daughters > 1 and not has_sons:
        return 2 / 3
    else:
        return 0
'''
4) Grand Daughter (from son only)
   a. Gets 1/2
      i. Deceased has only 1 Grand daughter from a son
      ii. Deceased does not have a son or a daughter
      iii. Deceased does not have a Grandson from a son
   b. Gets 2/3
      i. Deceased has multiple Granddaughters from a son
      ii. Deceased does not have a son or a daughter
      iii. Deceased does not have a Grandson from a son
   c. Gets 1/6 (H1)
      i. Deceased has just one daughter
      ii. Deceased does not have a son
      iii. Deceased does not have a Grandson from a son
'''
def grand_daughter_inheritance(num_grand_daughters, num_sons, num_daughters, has_grand_sons):
    if num_grand_daughters == 1 and not num_sons and not num_daughters and not has_grand_sons:
        return 0.5
    elif num_grand_daughters > 1 and not num_sons and not num_daughters and not has_grand_sons:
        return 2 / 3
    elif num_daughters == 1 and not num_sons and not has_grand_sons:
        return 1 / 6
    else:
        return 0
'''
5) Father [AnNisa 4:11]
   a. Gets 1/6
      i. Deceased has offspring
'''
def father_inheritance(has_offspring):
    if has_offspring:
        return 1 / 6
    else:
        return 0
'''
6) Mother [AnNisa 4:11]
   a. Gets 1/3
      i. Deceased does not have any offspring, and
      ii. Deceased does not have multiple siblings (full, paternal, maternal)
   b. Gets 1/6
      i. Deceased has offspring, or
      ii. Deceased has multiple siblings (full, paternal, maternal)
'''
def mother_inheritance(has_offspring, num_siblings):
    if not has_offspring and num_siblings < 2:
        return 1 / 3
    else:
        return 1 / 6
'''
7) Paternal Grand Father
   a. Gets 1/6
      i. Deceased does not have a father
      ii. Deceased has offspring
'''
def paternal_grand_father_inheritance(has_father, has_offspring):
    if not has_father and has_offspring:
        return 1 / 6
    else:
        return 0

'''
8) Paternal Grand Mother
   a. Gets 1/6
      i. Deceased does not have a mother
      ii. Deceased does not have a father
      iii. Deceased does not have a maternal grandmother
   b. Gets 1/12
   i. Deceased does not have a mother
   ii. Deceased does not have a father
   iii. Deceased has a maternal grandmother
'''
def paternal_grand_mother_inheritance(has_mother, has_father, has_maternal_grandmother):
    if not has_mother and not has_father:
        if has_maternal_grandmother:
            return 1 / 12
        else:
            return 1 / 6
    else:
        return 0
'''
9) Maternal Grand Mother
   a. Gets 1/6
      i. Deceased does not have a mother
   b. Gets 1/12
      i. Deceased does not have a mother
      ii. Deceased does not have a father
      iii. Deceased has a paternal grandmother
'''
def maternal_grand_mother_inheritance(has_mother, has_father, has_paternal_grandmother):
    if not has_mother:

        if has_father:
            # TODO: What does a father do to her ?
            return 0
        else:
            if has_paternal_grandmother:
                return 1 / 12
            else:
                return 1 / 6
    else:
        return 0
'''
10) Full Sister
   a. Gets ½ [AnNisa 4:176]
      i. Deceased has only 1 full sister
      ii. Deceased does not have any offspring
      iii. Deceased does not have any male paternal ancestor
      iv. Deceased does not have any full brother
   b. Gets 2/3 [AnNisa 4:176]
      i. Deceased has multiple full sisters
      ii. Deceased does not have any offspring
      iii. Deceased does not have any male paternal ancestor
      iv. Deceased does not have any full brother
'''
def full_sister_inheritance(num_full_sisters, has_offspring, has_male_paternal_ancestor, has_full_brother):
    if not has_offspring and not has_male_paternal_ancestor and not has_full_brother:
        if num_full_sisters == 1:
            return 0.5
        elif num_full_sisters > 1:
            return 2 / 3
    return 0
'''
11) Paternal Sister
   a. Gets 1/2
      i. Deceased has only 1 paternal sister
      ii. Deceased does not have any offspring
      iii. Deceased does not have any male paternal ancestor
      iv. Deceased does not have any full brother, full sister or paternal brother
   b. Gets 2/3
      i. Deceased has multiple paternal sisters
      ii. Deceased does not have any offspring
      iii. Deceased does not have any male paternal ancestor
      iv. Deceased does not have any full brother, full sister or paternal brother
   c. Gets 1/6
      i. Deceased has just 1 full sister
      ii. Deceased does not have any offspring
      iii. Deceased does not have any male paternal ancestor
      iv. Deceased does not have any full brother or paternal brother
'''
def paternal_sister_inheritance(num_paternal_sisters, num_full_sisters, has_offspring, has_male_paternal_ancestor,
                                has_full_brother, has_paternal_brother):
    if not has_offspring and not has_male_paternal_ancestor and not has_full_brother and not has_paternal_brother:
        if num_paternal_sisters == 1:
            return 0.5
        elif num_paternal_sisters > 1:
            return 2 / 3
        elif num_full_sisters == 1:
            return 1 / 6
    return 0
'''
12) Maternal Sibling [AnNisa 4:12]
   a. Gets 1/6
      i. Deceased has only 1 maternal sibling
      ii. Deceased does not have any male offspring
      iii. Deceased does not have any male paternal ancestors
   b. Gets 1/3
      i. Deceased has multiple maternal siblings
      ii. Deceased does not have any male offspring
      iii. Deceased does not have any male paternal ancestors Residual Shares (H2)
'''
def maternal_sibling_inheritance(num_maternal_siblings, has_male_offspring, has_male_paternal_ancestor):
    if not has_male_offspring and not has_male_paternal_ancestor:
        if num_maternal_siblings == 1:
            return 1 / 6
        elif num_maternal_siblings > 1:
            return 1 / 3
    return 0
'''
13) Blocking Rules
   a. Son blocks Paternal Grandson, Paternal Granddaughter, Full brother, Full sister, Paternal brother, Paternal sister, Maternal Brother, Maternal sister, Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   b. Grandson blocks Full brother, Full sister, Paternal brother, Paternal sister, Maternal Brother, Maternal sister, Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   c. Father blocks Paternal Grandfather, Paternal Grandmother, Full brother, Full sister, Paternal brother, Paternal sister, Maternal Brother, Maternal sister, Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   d. Mother blocks Paternal Grandmother, Maternal Grandmother
   e. Grandfather blocks Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   f. Full brother blocks Paternal brother, Paternal sister, Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   g. Full sister blocks Paternal brother, Paternal sister, ,Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son(can block only if the deceased has at least 1 female offspring, otherwise stuck in 2/3 zone)
   h. Paternal brother blocks Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   i. Paternal sister blocks Full Nephew, Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son(can block only if the deceased has either at least 1 female offspring or at least 2 sisters, otherwise stuck in 2/3 zone)
   j. Full Nephew blocks Paternal Nephew, Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   k. Paternal Nephew blocks Full Nephew’s son, Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   l. Full Nephew’s son blocks Paternal Nephew’s son, Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   m. Paternal Nephew’s son blocks Full paternal Uncle, Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   n. Full paternal Uncle blocks Paternal paternal uncle, Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   o. Paternal paternal uncle blocks Full cousin, Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   p. Full cousin blocks Paternal Cousin, Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   q. Paternal Cousin blocks Full cousin’s son, Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   r. Full cousin’s son blocks Paternal Cousin’s son, Full cousin’s son’s son, Paternal Cousin’s son’s son
   s. Paternal Cousin’s son blocks Full cousin’s son’s son, Paternal Cousin’s son’s son
   t. Full cousin’s son’s son blocks Paternal Cousin’s son’s son
'''
def can_inherit(heir, blocked_by):
    if heir == "son":
        if blocked_by in ["paternal grandson", "paternal granddaughter", "full brother", "full sister",
                          "paternal brother", "paternal sister", "maternal brother", "maternal sister", "full nephew",
                          "paternal nephew", "full nephew's son", "paternal nephew's son", "full paternal uncle",
                          "paternal paternal uncle", "full cousin", "paternal cousin", "full cousin's son",
                          "paternal cousin's son", "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "grandson":
        if blocked_by in ["full brother", "full sister", "paternal brother", "paternal sister", "maternal brother",
                          "maternal sister", "full nephew", "paternal nephew", "full nephew's son",
                          "paternal nephew's son", "full paternal uncle", "paternal paternal uncle", "full cousin",
                          "paternal cousin", "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "father":
        if blocked_by in ["paternal grandfather", "paternal grandmother", "full brother", "full sister",
                          "paternal brother", "paternal sister", "maternal brother", "maternal sister", "full nephew",
                          "paternal nephew", "full nephew's son", "paternal nephew's son", "full paternal uncle",
                          "paternal paternal uncle", "full cousin", "paternal cousin", "full cousin's son",
                          "paternal cousin's son", "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "mother":
        if blocked_by in ["paternal grandmother", "maternal grandmother"]:
            return False
    elif heir == "grandfather":
        if blocked_by in ["full nephew", "paternal nephew", "full nephew's son", "paternal nephew's son",
                          "full paternal uncle", "paternal paternal uncle", "full cousin", "paternal cousin",
                          "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "full brother":
        if blocked_by in ["paternal brother", "paternal sister", "full nephew", "paternal nephew", "full nephew's son",
                          "paternal nephew's son", "full paternal uncle", "paternal paternal uncle", "full cousin",
                          "paternal cousin", "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "full sister":
        if blocked_by in ["paternal brother", "paternal sister", "full nephew", "paternal nephew", "full nephew's son",
                          "paternal nephew's son", "full paternal uncle", "paternal paternal uncle", "full cousin",
                          "paternal cousin", "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "paternal brother":
        if blocked_by in ["full nephew", "paternal nephew", "full nephew's son", "paternal nephew's son",
                          "full paternal uncle", "paternal paternal uncle", "full cousin", "paternal cousin",
                          "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "paternal sister":
        if blocked_by in ["full nephew", "paternal nephew", "full nephew's son", "paternal nephew's son",
                          "full paternal uncle", "paternal paternal uncle", "full cousin", "paternal cousin",
                          "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "full nephew":
        if blocked_by in ["paternal nephew", "full nephew's son", "paternal nephew's son", "full paternal uncle",
                          "paternal paternal uncle", "full cousin", "paternal cousin", "full cousin's son",
                          "paternal cousin's son", "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "paternal nephew":
        if blocked_by in ["full nephew's son", "paternal nephew's son", "full paternal uncle",
                          "paternal paternal uncle", "full cousin", "paternal cousin", "full cousin's son",
                          "paternal cousin's son", "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "full nephew's son":
        if blocked_by in ["paternal nephew's son", "full paternal uncle", "paternal paternal uncle", "full cousin",
                          "paternal cousin", "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "paternal nephew's son":
        if blocked_by in ["full paternal uncle", "paternal paternal uncle", "full cousin", "paternal cousin",
                          "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "full paternal uncle":
        if blocked_by in ["paternal paternal uncle", "full cousin", "paternal cousin", "full cousin's son",
                          "paternal cousin's son", "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "paternal paternal uncle":
        if blocked_by in ["full cousin", "paternal cousin", "full cousin's son", "paternal cousin's son",
                          "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "full cousin":
        if blocked_by in ["paternal cousin", "full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "paternal cousin":
        if blocked_by in ["full cousin's son", "paternal cousin's son", "full cousin's son's son",
                          "paternal cousin's son's son"]:
            return False
    elif heir == "full cousin's son":
        if blocked_by in ["paternal cousin's son", "full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "paternal cousin's son":
        if blocked_by in ["full cousin's son's son", "paternal cousin's son's son"]:
            return False
    elif heir == "full cousin's son's son":
        if blocked_by == "paternal cousin's son's son":
            return False
    return True
'''
14) Tasib ranking in order
1) Son, daughter 2) Paternal Grandson, paternal Granddaughter 3) Father 4) Full Brother, Full sister (Kalaalah starts here) 5) Paternal Brother, Paternal Sister 6)
 Paternal Grandfather 7) Full brother’s son 8) Paternal brother’s son 9) Full brother’s son’s son 10) Paternal brother son’s son 11) Paternal uncle (father’s full brother) 
 12) Paternal paternal uncle (father’s paternal brother) 
 13) Paternal uncle’s son (father’s brother’s son) 14) Paternal paternal uncle’s son (father’s paternal brother’s son) 
 15) Paternal uncle’s son’s son (father’s brother’s son’ s son) 16) Paternal paternal uncle’s son’s son (father’s paternal brother’s son’s son) 
 17) Paternal uncle’s son’s son’s son (father’s brother’s son’ s son’s son) 18) Paternal paternal uncle’s son’s son’s son (father’s paternal brother’s son’s son’s son) 
 19) Emancipator 20) Emancipator’s independent Aaseebs
'''
def get_inheritance_priority(heir):
    if heir == "son" or heir == "daughter":
        return 1
    elif heir == "paternal grandson" or heir == "paternal granddaughter":
        return 2
    elif heir == "father":
        return 3
    elif heir == "full brother" or heir == "full sister":
        return 4
    elif heir == "paternal brother" or heir == "paternal sister":
        return 5
    elif heir == "paternal grandfather":
        return 6
    elif heir == "full brother's son":
        return 7
    elif heir == "paternal brother's son":
        return 8
    elif heir == "full brother's son's son":
        return 9
    elif heir == "paternal brother's son's son":
        return 10
    elif heir == "paternal uncle":
        return 11
    elif heir == "paternal paternal uncle":
        return 12
    elif heir == "paternal uncle's son":
        return 13
    elif heir == "paternal paternal uncle's son":
        return 14
    elif heir == "paternal uncle's son's son":
        return 15
    elif heir == "paternal paternal uncle's son's son":
        return 16
    elif heir == "paternal uncle's son's son's son":
        return 17
    elif heir == "paternal paternal uncle's son's son's son":
        return 18
    elif heir == "emancipator":
        return 19
    elif heir == "emancipator's independent Aaseebs":
        return 20
    else:
        return 0
'''
15) A male & female of the same class receive shares with the ration of 2:1 [AnNisa 4:11], [AnNisa 4:176]. The following conditions should be met.
   a. Male & female are of the same class
   b. This rule applies during the distribution of residual shares, and not the distribution of prescribed shares
   c. This rule doesn’t apply to maternal siblings. They are either ways given from prescribed shares
'''
# This rule doesn’t apply to maternal siblings. They are either ways given from prescribed shares TODO: what does this mean ?
def get_residual_share(heir, gender):
    if gender == "male" and (heir != "maternal brother" and heir != "maternal sister"):
        return 2
    elif gender == "female" and (heir != "maternal brother" and heir != "maternal sister"):
        return 1
    else:
        return 0
'''
16) If an heir is given the prescribed share, he/she drops from Ta’seeb if there are other Aaseebs qualified for inheritance a. Father is an exception to this rule
'''
'''
17) A father, or a grandfather, can never be cutoff by the heirs with prescribed shares.
'''
def drops_out_of_tasib(heir, has_prescribed_share):
    if has_prescribed_share and (heir != "father" and heir != "grandfather"):
        return True
    else:
        return False
'''
18) In the ‘Awal case, when the total is more than 1, all shares should be reduced proportionately so that the total shares is 1
   a. In case of Awal, and in the presence of Grandfather, sisters will be removed from the 2/3rd zone.
    Grandfather & sisters then will divide in the ratio of 2:1. (Disturbing Case) )
'''
def reduce_shares(heirs, total_shares, has_grandfather):
    if total_shares > 1:

        reduction_factor = 1 / total_shares
        for heir in heirs:
            heirs[heir] = heirs[heir] * reduction_factor

    # TODO: not the right logic
    # Check if the grandfather is present
    if has_grandfather:
        # Check if there are sisters present in the 2/3rd zone
        if "sisters" in heirs:
            # Remove the sisters from the 2/3rd zone
            del heirs["sisters"]
            # Calculate the grandfather's share based on the 2:1 ratio
            grandfather_share = 2 / 3
            # Calculate the sisters' share based on the 2:1 ratio
            sisters_share = 1 / 3
            # Add the grandfather's and sisters' shares to the heirs dictionary
            heirs["grandfather"] = grandfather_share
            heirs["sisters"] = sisters_share

    return heirs
'''
19) In Radd case, when the total is less than 1, all shares, except the shares of the spouse, 
    should be increased proportionately so that the total share is 1. 
    The spouse shares are strictly fixed. They cannot be increased unless no far relatives are found.
'''
def increase_shares(heirs, total_shares, has_far_relatives):
    if total_shares < 1:
        increase_factor = 1 / total_shares
        for heir in heirs:
            if heir != "spouse":
                heirs[heir] = heirs[heir] * increase_factor
    if not has_far_relatives:
        spouse_share = heirs["spouse"]
        spouse_share = spouse_share + (1 - total_shares)
        heirs["spouse"] = spouse_share
    return heirs
'''
20) If husband is also a paternal cousin (or his offspring), or an emancipator (or his relative), 
    he should be treated as two individuals and distribution should be made for each (if qualified)
'''
# not applicable, will be entered two time from thew user ?!
'''
21) If the deceased left behind a spouse, a father and a mother, but no offspring & multiple siblings, Umar’s calculations need to be applied. (Umar’s Fatawa)
   a. Parents will not get their prescribed share
   b. Parents will share the remainder with the 2:1 ratio for father & mother
   c. Multiple siblings can reduce mother’s share so Umar’s case will no longer be valid
'''
# TODO: will we handle this ??
'''
22) A full brother cannot receive less than the maternal brother
   a. Full brothers should share equally with the maternal siblings. Effectively, full brothers are treated as maternal siblings.
   b. This doesn’t apply to paternal brother (becoming maternal brother)
'''
# TODO: not right i guess
def equalize_full_brothers(heirs):
    if "full brother" in heirs and "maternal brother" in heirs:
        total_brother_share = heirs["full brother"] + heirs["maternal brother"]
        full_brother_share = total_brother_share / 2
        maternal_brother_share = total_brother_share / 2
        heirs["full brother"] = full_brother_share
        heirs["maternal brother"] = maternal_brother_share
    return heirs
'''
23) If the deceased did not leave behind a father or offspring, but left behind at least grandfather & siblings, he has a special case
   a. A=1/6 of the estate
   b. B=1/3 of the remainder of shares
   c. C=Treat grandfather like a brother and divide the shares equally among them
   d. The grandfather will be given the maximum of A, B and C
   e. If the grandfather’s share is causing the total shares to exceed 1, then the regular share of 1/6 will be given and the max of A, B, C rule will be ignored
   f. If the fractions sum exceeds 1, Awal should be applied; Grandfather’s share is not Ta’seeb in this case.
   g. During this calculation, Full Sister & paternal sister ‘s share should be excluded (if they are in 2/3rd zone)
'''
def calculate_grandfather_share(heirs, has_offspring, num_siblings):
    # Check if the deceased has no offspring
    if not has_offspring:
        # Calculate the total share of all heirs except the grandfather
        total_share = sum(heirs.values())
        # Calculate the share of the grandfather based on the A, B, and C rules
        A = 1 / 6
        B = (1 - total_share) / 3
        C = total_share / (num_siblings + 1)
        # Determine the maximum of A, B, and C
        grandfather_share = max(A, B, C)
        # Check if the grandfather's share is causing the total shares to exceed 1
        if total_share + grandfather_share > 1:
            # Set the grandfather's share to the regular share of 1/6
            grandfather_share = 1 / 6
        # Check if the fractions sum exceeds 1
        if total_share + grandfather_share > 1:
            # Apply Awal to reduce the shares proportionately
            reduction_factor = 1 / (total_share + grandfather_share)
            for heir in heirs:
                heirs[heir] *= reduction_factor
            # TODO: is this the right logic, and if it is move it to the right place
            # Exclude the share of the full sister and paternal sister if they are in the 2/3rd zone
            if "full sister" in heirs:
                del heirs["full sister"]
            if "paternal sister" in heirs:
                del heirs["paternal sister"]
        # Add the grandfather's share to the heirs dictionary
        heirs["grandfather"] = grandfather_share
    # Return the updated heirs dictionary
    return heirs
'''
24) If the deceased did not leave behind a father or offspring or brother, but left behind at least a grandfather and a sister. 
If a sister gets more than grandfather, then the shares should be readjusted
   a. Discard the prescribed share of the sister
   b. Sister & grandfather should share the remainder of estate with the ratio 1:2 Far Relatives
'''
def readjust_grandfather_sister_shares(heirs, has_father, has_offspring, has_brother):
    # Check if the deceased has no father, offspring, or brother
    if not has_father and not has_offspring and not has_brother:
        # Check if the heirs dictionary contains both a sister and a grandfather
        if "sister" in heirs and "grandfather" in heirs:
            # Calculate the total share of all heirs except the sister and grandfather
            total_share = sum(heirs.values()) - heirs["sister"] - heirs["grandfather"]
            # Check if the sister's share is greater than the grandfather's share
            if heirs["sister"] > heirs["grandfather"]:
                # Discard the prescribed share of the sister
                # total_share += heirs["sister"] ??
                heirs["sister"] = 0
                # Sister and grandfather should share the remainder of the estate with the ratio 1:2
                sister_share = total_share / 3
                grandfather_share = total_share * 2 / 3
                # Update the heirs dictionary with the calculated shares
                heirs["sister"] = sister_share
                heirs["grandfather"] = grandfather_share
    # Return the updated heirs dictionary
    return heirs
'''
25) Divide the inheritance to non-standard far relatives replacing themselves with the link they are attached to who is qualified for the inheritance..
'''
# TODO: will not allow the user to enter any non-stander people
'''
26) If there is still a remainder, then the remaining can now be given to the spouse if alive
'''
# TODO: convert to husband and wife and see when should you run it
def give_remainder_to_spouse(heirs, spouse):
    total_share = sum(heirs.values())
    if total_share < 1:
        remainder = 1 - total_share
        if spouse in heirs:
            heirs[spouse] += remainder

    return heirs
'''
27) If the deceased has obsoletely no relatives, the Islamic state takes the entire estate.
'''
def give_estate_to_islamic_state(heirs):
    # Check if the heirs dictionary is empty
    if not heirs:
        # Return a dictionary with the Islamic state as the only heir
        return {"Islamic state": 1}
    # Return the original heirs dictionary
    return heirs
'''
28) In case of female heirs, the inheritance stops at them and does not move on to their children as in case of male heirs.
'''
def remove_children_of_female_heirs(heirs):
    female_heirs = [heir for heir, share in heirs.items() if "daughter" == heir or "sister" == heir]
    for female_heir in female_heirs:
        heirs = {heir: share for heir, share in heirs.items() if female_heir not in heir and heir != "sister" and heir != "daughter"}
    return heirs
'''
29) In the absence of immediate children, grandchildren replace them as heirs
'''
def replace_children_with_grandchildren(heirs):
    if "son" not in heirs and "daughter" not in heirs:
        heirs = {heir: share for heir, share in heirs.items() if "grandson" in heir or "granddaughter" in heir}
    return heirs
'''
30) The 2/3 zone
   a. Certain female relatives can get into this zone
   b. The 4 possible relatives in this zone are – daughter, paternal granddaughter, full sister, paternal sister
   c. When a heir is inside this zone, she cannot block any body
   d. The male sibling of the same class can get her out of the 2/3 zone
      i. Son for the daughter
      ii. Paternal grandson for the paternal granddaughter
      iii. Full brother for the full sister
      iv. Paternal brother for the paternal sister
   e. Female offspring can never be together with female siblings in the 2/3 zone. The female offspring can get the female siblings out of the 2/3 zone
   f. Daughter & granddaughter cannot be given the same share when in 2/3 zone. Same applies for full sister & paternal sister. One is given ½ & the other is given 1/6.
   g. Full brother can get the paternal sister out of 2/3 zone, actually completely blocks her.
'''
# TODO: should be used in other rules ?
'''
31) The 2/3 fraction is either for daughter-granddaughter, or, full sister-paternal sister. The 2/3 can never be shared between female offspring & female siblings
'''
# TODO: what to do with this ?
'''
32) Maternal siblings can reduce mother’s share
33) Maternal siblings do not have 1:2 male female ratio
'''
def reduce_mothers_share(heirs):
    # Check if there are both male and female maternal siblings present
    if "maternal brother" in heirs and "maternal sister" in heirs:
        # Check if the mother is present
        if "mother" in heirs:
            # Calculate the total share of the maternal siblings
            maternal_sibling_share = sum([share for heir, share in heirs.items() if "maternal" in heir])
            # Calculate the new share of the mother
            mother_share = heirs["mother"] - maternal_sibling_share
            # Update the share of the mother in the heirs dictionary
            heirs["mother"] = mother_share
            # Calculate the new share of the maternal siblings 1:1
            # TODO: fix this, they are all the same i guess
            male_maternal_sibling_share = 0.5 * maternal_sibling_share
            female_maternal_sibling_share = 0.5 * maternal_sibling_share
            # Update the share of the male and female maternal siblings in the heirs dictionary
            heirs["maternal brother"] = male_maternal_sibling_share
            heirs["maternal sister"] = female_maternal_sibling_share
    # Return the updated heirs dictionary
    return heirs
'''
34) Father blocks full siblings, paternal siblings, and maternal siblings
'''
def block_siblings_if_father_exisit(heirs):
    if "father" in heirs:
        heirs = {heir: share for heir, share in heirs.items() if "full" not in heir}
        heirs = {heir: share for heir, share in heirs.items() if "paternal" not in heir}
        heirs = {heir: share for heir, share in heirs.items() if "maternal" not in heir}

    return heirs
'''
35) Following relatives can never be blocked
   • Husband
   • Wife
   • Father
   • Mother
   • Son
   • Daughter
'''
def get_unblocked_relatives(heirs):
    # Remove all heirs except for the husband, wife, father, mother, son, and daughter
    heirs = {heir: share for heir, share in heirs.items() if
             heir in ("husband", "wife", "father", "mother", "son", "daughter")}
    # Return the updated heirs dictionary
    return heirs
'''
37) Spouse share can never be increased, even if there are no more standard heirs left. 
    The far relatives are given priority first before increasing spouse’s share are
'''
# TODO: What to do with this ? check if husband or wife are the only relative and give them the rest
'''
38) Role promotion when the person is not alive
   • Grandfather becomes a father
   • Paternal grandmother becomes a mother
   • Granddaughter become a daughter
   • Sister becomes a daughter
   • Paternal sister becomes a daughter
'''
# TODO: is this the right way ?
def promote_heirs(heirs):
    if "father" not in heirs and "grandfather" in heirs:
        heirs["father"] = heirs.pop("grandfather")

    if "mother" not in heirs and "paternal grandmother" in heirs:
        heirs["mother"] = heirs.pop("paternal grandmother")

    if "daughter" not in heirs and "granddaughter" in heirs:
        heirs["daughter"] = heirs.pop("granddaughter")

    elif "daughter" not in heirs and "sister" in heirs:
        heirs["daughter"] = heirs.pop("sister")

    elif "daughter" not in heirs and "paternal sister" in heirs:
        heirs["daughter"] = heirs.pop("paternal sister")

    return heirs
'''
39) Maternal grandfather (mother’s father) is blocked from inheritance. His both male & female ancestors are also blocked. 
    This is different from maternal grandmother (mother’s mother). She gets the inheritance. 
    Also, her female ancestors can also get inheritance, but not the male ancestors.
'''
# TODO: we will not allow the user to enter these people in the first place, right ??
'''
40) The only female chain that continues indefinitely is mother’s mother’s mother’s ….
'''
# TODO: we will just the first two right ?!
def is_female_ancestor_in_indefinite_chain(relative):
    if relative in ["mother", "grandmother", "great-grandmother", "great-great-grandmother"]:
        return True
    return False
'''
41) There is a difference of opinion on father blocking the father’s mother. However, all agree that a mother can block father’s mother.
'''
# TODO: what to do with this ? nothing or take one opinion
'''
42) There is some difference of opinion on grandfather blocking the siblings
'''
# TODO: what to do with this ? nothing or take one opinion
'''
43) Following relatives are not qualified for Ta’seeb
   • Mother
   • Paternal grandmother
   • Maternal grandmother
   • Husband
   • Wife
   • Maternal Brother
   • Maternal Sister
'''
def is_qualified_for_taseeb(relative):
    not_qualified = ['Mother', 'Paternal grandmother', 'Maternal grandmother', 'Husband', 'Wife', 'Maternal Brother',
                     'Maternal Sister']
    if relative in not_qualified:
        return False
    else:
        return True
'''
44) Joint Ta’seebs are possible only for the following casess
 • Son & daughter
 • Grandson & Grand daughter
 • Full brother & full sister
 • Paternal brother & paternal sister
'''
def are_joint_taseebs_possible(relative1, relative2):
    if (relative1, relative2) in [("son", "daughter"), ("grandson", "granddaughter"), ("full brother", "full sister"),
                                  ("paternal brother", "paternal sister")]:
        return True
    return False
