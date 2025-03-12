
import pytest
from app import NLPDemo

def test_nlp_demo_initialization():
    """Test the initialization of NLPDemo class."""
    demo = NLPDemo()
    assert hasattr(demo, 'available_nlp_tasks')
    assert len(demo.available_nlp_tasks) == 4
    assert all(isinstance(task, dict) for task in demo.available_nlp_tasks)
    assert all('name' in task and 'description' in task for task in demo.available_nlp_tasks)

def test_preprocess_text_tokenization():
    """Test tokenization preprocessing."""
    demo = NLPDemo()
    text = "This is a test sentence."
    options = {'tokenize': True, 'stop_words': False, 'stem': False, 'lemmatize': False}
    
    processed_text, visualizations = demo.preprocess_text(text, options)
    
    assert processed_text is not None
    assert len(visualizations) == 1
    assert visualizations[0][0] == 'Tokens'
    assert len(visualizations[0][1]) >= 5  # At least 5 tokens in the test sentence

def test_preprocess_text_multiple_options():
    """Test multiple preprocessing options together."""
    demo = NLPDemo()
    text = "Running and jumped are action words."
    options = {'tokenize': True, 'stop_words': True, 'stem': True, 'lemmatize': False}
    
    processed_text, visualizations = demo.preprocess_text(text, options)
    
    assert processed_text is not None
    assert len(visualizations) == 3  # Should have tokenization, stop words, and stemming
