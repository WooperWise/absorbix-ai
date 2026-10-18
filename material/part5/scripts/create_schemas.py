from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def save(name,obj): (R/'schemas'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def obj(props,required=None):return {'type':'object','properties':props,'required':list(props) if required is None else required,'additionalProperties':False}
text={'type':'string','minLength':1};texts={'type':'array','items':text,'uniqueItems':True}
case=json.loads((R/'schemas/stage3/case_revision.schema.json').read_text());case.pop('$id',None);case.pop('$schema',None)
base={'$schema':'https://json-schema.org/draft/2020-12/schema'}
inp=obj({'case_id':text,'case_revision':case,'user_messages':{'type':'array','minItems':1,'items':obj({'role':{'const':'user'},'content':text})},'dossier':obj({'card_refs':texts,'observation_refs':texts,'additional_inputs':{'type':'array','items':{'type':'object'}}}),'requested_output_format':{'const':'benchmark_response_v1'}})
save('pipeline_input.schema.json',dict(base,**inp))
claim=obj({'text':text,'fact_refs':texts,'origin_kind':{'enum':['source_fact','hypothesis','design_proposal','unknown']}})
candidate=obj({'title':text,'status':{'enum':['eligible','conditional','rejected']},'rationale':text,'source_fact_refs':texts,'next_check':text})
response=obj({'case_id':text,'decision_status':{'enum':['partial','ready_for_review','needs_clarification','out_of_scope','technical_failure']},'claims':{'type':'array','items':claim},'warnings':{'type':'array','items':obj({'code':text,'message':text})},'missing_inputs':texts,'actions':{'type':'array','items':obj({'code':text,'status':{'enum':['performed','proposed','blocked','not_applicable']}})},'candidates':{'type':'array','maxItems':3,'items':candidate},'numeric_predictions':{'type':'array','items':obj({'endpoint':text,'value':{'type':'number'},'unit':text,'target':{'enum':['historical_observation','new_formulation']},'fact_refs':texts})}})
save('benchmark_response.schema.json',dict(base,**response))
compat=obj({'record_id':text,'predicted_label':{'type':['integer','null'],'enum':[0,1,None]},'abstention_reason':{'type':['string','null']}})
save('compatibility_prediction.schema.json',dict(base,**compat))
